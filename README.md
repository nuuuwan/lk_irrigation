# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_19:46:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,942 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 19:46:02 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:21:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.80 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-05-13 19:10:50 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-13 19:10:48 | Moraketiya (Walawe Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:10:46 | Moraketiya (Walawe Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:10:24 | Moraketiya (Walawe Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:08:39 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-13 19:07:37 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.018 |  |
| 2026-05-13 19:06:53 | Rathnapura (Kalu Ganga) | 6.03 | 🟡 Alert | -0.066 |  |
| 2026-05-13 19:06:27 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | -0.078 |  |
| 2026-05-13 19:06:03 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:05:39 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.029 |  |
| 2026-05-13 19:05:21 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-13 19:04:59 | Thanamalwila (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-05-13 19:04:46 | Moragaswewa (Deduru Oya) | 2.82 | 🟢 Normal | -0.039 |  |
| 2026-05-13 19:04:38 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-13 19:04:33 | Magura (Kalu Ganga) | 5.17 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-13 19:04:15 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | -0.042 |  |
| 2026-05-13 19:04:08 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-13 19:03:59 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:03:39 | Baddegama (Gin Ganga) | 3.11 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-13 19:03:38 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-05-13 19:03:26 | Thawalama (Gin Ganga) | 2.97 | 🟢 Normal | -0.171 |  |
| 2026-05-13 19:03:18 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.041 |  |
| 2026-05-13 19:03:17 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-05-13 19:03:15 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:03:08 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:02:58 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.060 |  |
| 2026-05-13 19:02:52 | Dunamale (Aththanagalu Oya) | 3.48 | 🟡 Alert | 0.000 |  |
| 2026-05-13 19:02:48 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-05-13 19:02:47 | Putupaula (Kalu Ganga) | 2.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 19:02:45 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:02:39 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:02:34 | Dunamale (Aththanagalu Oya) | 3.48 | 🟡 Alert | 0.000 |  |
| 2026-05-13 19:02:20 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:02:13 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:02:03 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.050 |  |
| 2026-05-13 19:01:58 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:00:37 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 19:21:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.80 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-05-13 19:04:33 | Magura (Kalu Ganga) | 5.17 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-13 19:02:52 | Dunamale (Aththanagalu Oya) | 3.48 | 🟡 Alert | 0.000 |  |
| 2026-05-13 19:04:15 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | -0.042 |  |
| 2026-05-13 19:06:53 | Rathnapura (Kalu Ganga) | 6.03 | 🟡 Alert | -0.066 |  |
| 2026-05-13 18:08:14 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | 12.000 | 🔺 Rising |
| 2026-05-13 19:04:38 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-13 19:08:39 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-13 18:02:23 | Galgamuwa (Mee Oya) | 2.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-13 19:10:50 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-13 19:03:39 | Baddegama (Gin Ganga) | 3.11 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-13 19:04:08 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-13 19:05:21 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-13 19:00:37 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 19:02:47 | Putupaula (Kalu Ganga) | 2.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-13 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 19:01:58 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:46:02 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:02:39 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:03:15 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:02:45 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:06:03 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:10:48 | Moraketiya (Walawe Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:03:59 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:02:13 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:03:08 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-05-13 19:03:38 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.009 |  |
| 2026-05-13 19:04:59 | Thanamalwila (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-05-13 19:03:17 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-05-13 19:07:37 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.018 |  |
| 2026-05-13 19:02:48 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-05-13 19:05:39 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.029 |  |
| 2026-05-13 19:04:46 | Moragaswewa (Deduru Oya) | 2.82 | 🟢 Normal | -0.039 |  |
| 2026-05-13 19:03:18 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.041 |  |
| 2026-05-13 19:02:03 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.050 |  |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-13 19:02:58 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.060 |  |
| 2026-05-13 19:06:27 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | -0.078 |  |
| 2026-05-13 19:03:26 | Thawalama (Gin Ganga) | 2.97 | 🟢 Normal | -0.171 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)