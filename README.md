# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_09:11:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,733 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 09:11:46 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:10:38 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:07:03 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:06:42 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:06:41 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.019 |  |
| 2026-06-26 09:06:26 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-26 09:06:06 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:05:59 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.027 |  |
| 2026-06-26 09:05:48 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.010 |  |
| 2026-06-26 09:05:22 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:05:07 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:04:09 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:03:52 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | -0.040 |  |
| 2026-06-26 09:03:46 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:03:44 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 09:03:40 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.039 |  |
| 2026-06-26 09:03:19 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-06-26 09:03:09 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-06-26 09:03:08 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:03:06 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:03:02 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-06-26 09:03:01 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:02:47 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-06-26 09:02:46 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-26 09:02:45 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-26 09:02:29 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:02:23 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-06-26 09:02:22 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:02:20 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:02:19 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-06-26 09:02:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-26 09:02:10 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-06-26 09:02:08 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:02:07 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:02:07 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-26 09:01:43 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:01:05 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-06-26 09:00:23 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:00:19 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 08:57:39 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 09:02:47 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-06-26 09:02:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-26 09:02:46 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-26 09:02:07 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-26 09:02:45 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-26 09:06:26 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-26 09:03:44 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 09:00:19 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:04:09 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:07:03 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:03:08 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:02:20 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:10:38 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:05:07 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:03:01 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:03:06 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:03:46 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:05:22 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:02:07 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:02:29 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:11:46 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:02:08 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:02:22 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:06:06 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:01:43 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:00:23 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-06-26 09:03:19 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-06-26 09:05:48 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.010 |  |
| 2026-06-26 09:03:02 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-06-26 09:02:10 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-06-26 09:02:23 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-06-26 09:06:41 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | -0.019 |  |
| 2026-06-26 09:03:09 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-06-26 09:01:05 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-06-26 09:05:59 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.027 |  |
| 2026-06-26 09:02:19 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-06-26 09:03:40 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.039 |  |
| 2026-06-26 09:03:52 | Glencourse (Kelani Ganga) | 9.91 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)