# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_14:16:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,851 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 14:16:52 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-06-08 14:15:34 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -0.027 |  |
| 2026-06-08 14:10:04 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | -0.019 |  |
| 2026-06-08 14:09:22 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.010 |  |
| 2026-06-08 14:09:00 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:07:47 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:07:26 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:07:17 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-08 14:07:01 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.029 |  |
| 2026-06-08 14:06:41 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:06:34 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:04:32 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | -0.039 |  |
| 2026-06-08 14:04:20 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:03:53 | Hanwella (Kelani Ganga) | 3.23 | 🟢 Normal | -0.040 |  |
| 2026-06-08 14:03:30 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:03:29 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:03:25 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-06-08 14:03:24 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-06-08 14:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-08 14:03:17 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-06-08 14:03:08 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:02:51 | Putupaula (Kalu Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-06-08 14:02:41 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:02:40 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:02:39 | Ellagawa (Kalu Ganga) | 7.33 | 🟢 Normal | -0.059 |  |
| 2026-06-08 14:02:38 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:02:31 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-06-08 14:02:23 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.011 |  |
| 2026-06-08 14:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | -0.030 |  |
| 2026-06-08 14:02:16 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:01:57 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:01:46 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:01:42 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-08 14:01:38 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:01:30 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-08 14:01:20 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:01:12 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-08 14:01:01 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 14:03:18 | Nawalapitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-08 14:01:12 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-08 14:01:42 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-08 14:01:30 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-08 14:01:01 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 13:09:17 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 14:02:41 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:02:38 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:01:57 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:01:46 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:06:34 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:07:47 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:04:20 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:03:08 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:06:41 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:03:29 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:02:40 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:01:20 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:09:00 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:02:16 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:01:38 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:07:26 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:03:30 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-08 14:16:52 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-06-08 14:09:22 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.010 |  |
| 2026-06-08 14:07:17 | Deraniyagala (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-06-08 14:02:31 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-06-08 14:02:23 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.011 |  |
| 2026-06-08 14:10:04 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | -0.019 |  |
| 2026-06-08 14:03:24 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | -0.020 |  |
| 2026-06-08 14:02:51 | Putupaula (Kalu Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-06-08 14:03:25 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-06-08 14:15:34 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | -0.027 |  |
| 2026-06-08 14:07:01 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.029 |  |
| 2026-06-08 14:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | -0.030 |  |
| 2026-06-08 14:03:17 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-06-08 14:04:32 | Glencourse (Kelani Ganga) | 11.04 | 🟢 Normal | -0.039 |  |
| 2026-06-08 14:03:53 | Hanwella (Kelani Ganga) | 3.23 | 🟢 Normal | -0.040 |  |
| 2026-06-08 14:02:39 | Ellagawa (Kalu Ganga) | 7.33 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)