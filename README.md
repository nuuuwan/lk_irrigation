# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_15:03:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,007 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 15:03:07 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:03:00 | Deraniyagala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-05-28 15:02:56 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-05-28 15:02:24 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:02:23 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.23 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-28 15:02:17 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:02:02 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:01:49 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:01:40 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:01:34 | Magura (Kalu Ganga) | 4.86 | 🟡 Alert | 0.075 | 🔺 Rising |
| 2026-05-28 15:01:23 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 15:01:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:01:18 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:01:13 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | -0.011 |  |
| 2026-05-28 15:00:54 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:00:45 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-28 15:00:10 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:00:05 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-28 14:36:11 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-05-28 14:28:05 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | 2.866 | 🔺 Rising |
| 2026-05-28 14:18:31 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | 0.063 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 15:01:34 | Magura (Kalu Ganga) | 4.86 | 🟡 Alert | 0.075 | 🔺 Rising |
| 2026-05-28 15:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.23 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-28 14:28:05 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | 2.866 | 🔺 Rising |
| 2026-05-28 14:01:06 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.443 | 🔺 Rising |
| 2026-05-28 14:09:49 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-05-28 14:18:31 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-28 14:03:41 | Baddegama (Gin Ganga) | 2.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-28 15:01:23 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 14:05:49 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-28 14:09:42 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 14:09:18 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-28 15:01:18 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-05-28 14:03:35 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:02:17 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:01:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:00:10 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:01:49 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:03:00 | Deraniyagala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-28 14:09:57 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 14:07:22 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:00:05 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:02:02 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:02:24 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-28 14:02:30 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-05-28 14:01:34 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:00:54 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:01:40 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:02:23 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:03:07 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-28 15:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-05-28 15:00:45 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-28 14:02:34 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-05-28 14:06:04 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-05-28 15:01:13 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | -0.011 |  |
| 2026-05-28 15:02:56 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-05-28 14:36:11 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-05-28 14:02:42 | Rathnapura (Kalu Ganga) | 3.82 | 🟢 Normal | -0.032 |  |
| 2026-05-28 14:04:29 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | -0.058 |  |
| 2026-05-28 14:02:31 | Hanwella (Kelani Ganga) | 4.01 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)