# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_12:39:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,825 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 12:39:10 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:37:08 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:28:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.040 |  |
| 2026-04-14 12:22:05 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-04-14 12:20:50 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.032 |  |
| 2026-04-14 12:19:38 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:17:40 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:14:55 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:09:49 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.012 |  |
| 2026-04-14 12:08:44 | Thanamalwila (Kirindi Oya) | 1.55 | 🟢 Normal | -0.023 |  |
| 2026-04-14 12:08:30 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:08:25 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:08:12 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:07:45 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:07:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-14 12:06:55 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-04-14 12:06:40 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-04-14 12:06:39 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | -0.053 |  |
| 2026-04-14 12:06:31 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:05:40 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-14 12:05:33 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:04:45 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-04-14 12:04:39 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-04-14 12:03:57 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.069 |  |
| 2026-04-14 12:03:35 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-14 12:03:34 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:03:16 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.029 |  |
| 2026-04-14 12:03:06 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-04-14 12:02:46 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:02:38 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:02:25 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.071 |  |
| 2026-04-14 12:02:18 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-04-14 12:01:51 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-04-14 12:01:19 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.005 |  |
| 2026-04-14 12:01:10 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.052 |  |
| 2026-04-14 12:00:45 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:00:41 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-04-14 12:00:32 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-14 12:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 12:00:07 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 12:06:55 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-04-14 12:04:39 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-04-14 12:22:05 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-04-14 12:07:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-14 10:01:40 | Moragaswewa (Deduru Oya) | 0.79 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-14 12:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 12:00:07 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:00:45 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:39:10 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:19:38 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:08:12 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-14 11:04:36 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:37:08 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:03:34 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:14:55 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:07:45 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:02:38 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:08:25 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:06:31 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 12:01:19 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.005 |  |
| 2026-04-14 12:05:40 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-14 12:00:32 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-14 12:03:35 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-14 12:00:41 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-04-14 12:01:51 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-04-14 12:09:49 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.012 |  |
| 2026-04-14 12:02:18 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-04-14 12:04:45 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-04-14 11:02:38 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.022 |  |
| 2026-04-14 12:08:44 | Thanamalwila (Kirindi Oya) | 1.55 | 🟢 Normal | -0.023 |  |
| 2026-04-14 12:03:16 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.029 |  |
| 2026-04-14 12:03:06 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-04-14 12:20:50 | Thalgahagoda (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.032 |  |
| 2026-04-14 12:28:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.040 |  |
| 2026-04-14 11:00:16 | Weraganthota (Mahaweli Ganga) | -2.89 | 🟢 Normal | -0.040 |  |
| 2026-04-14 12:01:10 | Thanthirimale (Malwathu Oya) | 4.17 | 🟢 Normal | -0.052 |  |
| 2026-04-14 12:06:39 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | -0.053 |  |
| 2026-04-14 12:03:57 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | -0.069 |  |
| 2026-04-14 12:02:25 | Rathnapura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)