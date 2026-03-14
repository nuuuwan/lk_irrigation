# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_21:15:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,453 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 21:15:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.023 |  |
| 2026-03-14 21:09:11 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.043 |  |
| 2026-03-14 21:08:29 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-14 21:08:04 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-03-14 21:07:45 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:07:25 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.028 |  |
| 2026-03-14 21:06:51 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:06:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:06:21 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.009 |  |
| 2026-03-14 21:06:04 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:06:02 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:05:48 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-03-14 21:05:46 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:05:32 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 21:05:01 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-14 21:04:42 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-03-14 21:04:29 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:03:42 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 21:02:56 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 21:02:52 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:02:50 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 21:02:47 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-03-14 21:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-14 21:02:31 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-03-14 21:02:31 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 21:02:29 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.021 |  |
| 2026-03-14 21:02:23 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:02:22 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:02:14 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:02:13 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:01:53 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:01:45 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-14 21:01:41 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:00:55 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.063 |  |
| 2026-03-14 21:00:48 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.021 |  |
| 2026-03-14 21:00:22 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:00:16 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:00:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 21:02:31 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-03-14 21:05:48 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-03-14 21:01:45 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-14 21:08:29 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-14 21:03:42 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 21:05:32 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 21:02:50 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 21:02:56 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 21:02:31 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 21:00:22 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:01:41 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:06:02 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:02:13 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:00:16 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:03:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:07:45 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:06:04 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:02:14 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:02:52 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:00:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:06:43 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:02:23 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:05:46 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:06:51 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:01:03 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:04:29 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-14 21:06:21 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.009 |  |
| 2026-03-14 21:02:47 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-03-14 21:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-14 21:05:01 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-03-14 21:02:29 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.021 |  |
| 2026-03-14 21:00:48 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | -0.021 |  |
| 2026-03-14 21:15:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.023 |  |
| 2026-03-14 21:07:25 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | -0.028 |  |
| 2026-03-14 21:04:42 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.030 |  |
| 2026-03-14 21:08:04 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-03-14 21:09:11 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.043 |  |
| 2026-03-14 21:00:55 | Manampitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.063 |  |
| 2026-03-14 18:01:50 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)