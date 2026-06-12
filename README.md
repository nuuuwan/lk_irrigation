# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_20:15:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,656 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 20:15:51 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-12 20:13:37 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:09:53 | Badalgama (Maha Oya) | 3.50 | 🟢 Normal | -0.019 |  |
| 2026-06-12 20:09:42 | Putupaula (Kalu Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:09:18 | Rathnapura (Kalu Ganga) | 6.75 | 🟡 Alert | 0.137 | 🔺 Rising |
| 2026-06-12 20:08:41 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 20:08:26 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-12 20:08:13 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:07:38 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:07:32 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-06-12 20:07:28 | Baddegama (Gin Ganga) | 2.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-12 20:06:40 | Panadugama (Nilwala Ganga) | 4.24 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-12 20:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.06 | 🟡 Alert | 0.033 | 🔺 Rising |
| 2026-06-12 20:06:08 | Hanwella (Kelani Ganga) | 3.84 | 🟢 Normal | -0.039 |  |
| 2026-06-12 20:06:06 | Thawalama (Gin Ganga) | 3.60 | 🟢 Normal | 0.636 | 🔺 Rising |
| 2026-06-12 20:05:32 | Urawa (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-12 20:05:29 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:05:23 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-12 20:05:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:05:12 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.096 |  |
| 2026-06-12 20:05:07 | Magura (Kalu Ganga) | 4.66 | 🟡 Alert | -0.009 |  |
| 2026-06-12 20:04:59 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:04:53 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:04:36 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-12 20:04:35 | Nawalapitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.152 |  |
| 2026-06-12 20:03:21 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-06-12 20:03:16 | Deraniyagala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.247 |  |
| 2026-06-12 20:03:08 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | -0.021 |  |
| 2026-06-12 20:02:26 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 20:02:22 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-06-12 20:02:18 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | -0.020 |  |
| 2026-06-12 20:01:52 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:01:44 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:01:33 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | 0.041 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 20:09:18 | Rathnapura (Kalu Ganga) | 6.75 | 🟡 Alert | 0.137 | 🔺 Rising |
| 2026-06-12 20:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.06 | 🟡 Alert | 0.033 | 🔺 Rising |
| 2026-06-12 20:05:07 | Magura (Kalu Ganga) | 4.66 | 🟡 Alert | -0.009 |  |
| 2026-06-12 20:06:06 | Thawalama (Gin Ganga) | 3.60 | 🟢 Normal | 0.636 | 🔺 Rising |
| 2026-06-12 20:07:32 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-06-12 20:04:36 | Glencourse (Kelani Ganga) | 11.70 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-12 20:05:32 | Urawa (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-12 20:15:51 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-06-12 20:08:26 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-12 20:06:40 | Panadugama (Nilwala Ganga) | 4.24 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-12 20:01:33 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-12 20:05:23 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-12 20:07:28 | Baddegama (Gin Ganga) | 2.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-12 18:04:11 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-12 20:02:26 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 20:08:41 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:00:13 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:04:59 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:07:38 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:01:44 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:13:37 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:04:53 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:05:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:05:29 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:09:42 | Putupaula (Kalu Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:01:52 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:19:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:08:13 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-06-12 20:03:21 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-06-12 20:02:22 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-06-12 20:09:53 | Badalgama (Maha Oya) | 3.50 | 🟢 Normal | -0.019 |  |
| 2026-06-12 20:02:18 | Dunamale (Aththanagalu Oya) | 3.06 | 🟢 Normal | -0.020 |  |
| 2026-06-12 20:03:08 | Giriulla (Maha Oya) | 2.40 | 🟢 Normal | -0.021 |  |
| 2026-06-12 20:06:08 | Hanwella (Kelani Ganga) | 3.84 | 🟢 Normal | -0.039 |  |
| 2026-06-12 20:00:16 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.043 |  |
| 2026-06-12 20:05:12 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.096 |  |
| 2026-06-12 20:04:35 | Nawalapitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.152 |  |
| 2026-06-12 20:03:16 | Deraniyagala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.247 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)