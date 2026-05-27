# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_22:13:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,393 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 22:13:23 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-27 22:12:47 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-27 22:09:44 | Magura (Kalu Ganga) | 4.32 | 🟡 Alert | 0.418 | 🔺 Rising |
| 2026-05-27 22:08:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.47 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-05-27 22:07:31 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 22:07:20 | Rathnapura (Kalu Ganga) | 4.75 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-05-27 22:07:05 | Dunamale (Aththanagalu Oya) | 2.41 | 🟢 Normal | -0.019 |  |
| 2026-05-27 22:06:41 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.069 |  |
| 2026-05-27 22:06:21 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:04:13 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:04:13 | Hanwella (Kelani Ganga) | 4.23 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-27 22:04:02 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-27 22:04:02 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:03:59 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:03:33 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:03:29 | Thawalama (Gin Ganga) | 3.05 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-27 22:03:25 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.011 |  |
| 2026-05-27 22:03:22 | Deraniyagala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.314 |  |
| 2026-05-27 22:03:14 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:03:03 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.097 |  |
| 2026-05-27 22:02:51 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:02:49 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:02:40 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.030 |  |
| 2026-05-27 22:02:39 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-27 22:02:27 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:02:07 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:01:56 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:01:47 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:01:44 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:01:17 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:01:16 | Glencourse (Kelani Ganga) | 12.35 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-05-27 22:01:14 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-05-27 22:00:53 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-05-27 22:00:52 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:00:48 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 22:09:44 | Magura (Kalu Ganga) | 4.32 | 🟡 Alert | 0.418 | 🔺 Rising |
| 2026-05-27 22:08:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.47 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-05-27 22:01:14 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-05-27 22:01:16 | Glencourse (Kelani Ganga) | 12.35 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2026-05-27 22:07:20 | Rathnapura (Kalu Ganga) | 4.75 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-05-27 22:03:29 | Thawalama (Gin Ganga) | 3.05 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-27 18:00:23 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-27 22:04:13 | Hanwella (Kelani Ganga) | 4.23 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-27 22:04:02 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-27 22:12:47 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-27 21:03:37 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-27 22:07:31 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 22:13:23 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-27 22:02:07 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:03:59 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:01:17 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:04:13 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:01:47 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:02:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:02:49 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:04:02 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:02:51 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:03:14 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:00:52 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:01:56 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:03:33 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:02:27 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:06:21 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 22:01:44 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 18:05:39 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.009 |  |
| 2026-05-27 22:02:39 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-27 22:03:25 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.011 |  |
| 2026-05-27 22:00:53 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.011 |  |
| 2026-05-27 22:07:05 | Dunamale (Aththanagalu Oya) | 2.41 | 🟢 Normal | -0.019 |  |
| 2026-05-27 21:04:16 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.029 |  |
| 2026-05-27 22:02:40 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.030 |  |
| 2026-05-27 22:06:41 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.069 |  |
| 2026-05-27 22:03:03 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.097 |  |
| 2026-05-27 22:03:22 | Deraniyagala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.314 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)