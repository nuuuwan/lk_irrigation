# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_19:19:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,335 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 19:19:41 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:18:02 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-07 19:14:58 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-01-07 19:13:06 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:09:34 | Urawa (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-01-07 19:07:58 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-01-07 19:07:33 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.009 |  |
| 2026-01-07 19:07:19 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -2.626 |  |
| 2026-01-07 19:06:38 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:06:29 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-07 19:05:51 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.075 |  |
| 2026-01-07 19:05:39 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:05:27 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-01-07 19:04:42 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-07 19:04:41 | Siyambalanduwa (Heda Oya) | 1.49 | 🟢 Normal | -0.040 |  |
| 2026-01-07 19:04:19 | Katharagama (Menik Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:04:07 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:03:46 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:03:34 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 19:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:03:29 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-01-07 19:03:23 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 19:02:52 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 19:02:46 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-01-07 19:02:44 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-07 19:02:41 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 19:02:31 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-07 19:02:17 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:02:10 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:02:09 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:02:06 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 19:02:01 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.062 |  |
| 2026-01-07 19:01:58 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-01-07 19:01:51 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:01:19 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:01:03 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -2.626 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 19:02:46 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-01-07 19:09:34 | Urawa (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-01-07 19:14:58 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-01-07 19:02:06 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 19:02:41 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 19:04:42 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-07 18:01:49 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 19:02:52 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 19:03:23 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 19:03:34 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 19:18:02 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-07 19:04:07 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:01:51 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:19:41 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:01:21 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:02:31 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:13:06 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:02:10 | Padiyathalawa (Maduru Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:03:46 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:02:17 | Dunamale (Aththanagalu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:04:19 | Katharagama (Menik Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:05:39 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:01:19 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:06:38 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-07 19:07:58 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-01-07 19:07:33 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.009 |  |
| 2026-01-07 19:06:29 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-07 19:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-07 19:02:44 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-07 19:05:27 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-01-07 19:03:29 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | -0.010 |  |
| 2026-01-07 19:01:58 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-01-07 18:03:25 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.023 |  |
| 2026-01-07 19:04:41 | Siyambalanduwa (Heda Oya) | 1.49 | 🟢 Normal | -0.040 |  |
| 2026-01-07 18:08:59 | Manampitiya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.041 |  |
| 2026-01-07 19:02:01 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.062 |  |
| 2026-01-07 19:05:51 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.075 |  |
| 2026-01-07 19:07:19 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -2.626 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)