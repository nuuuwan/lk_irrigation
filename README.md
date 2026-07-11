# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_23:04:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,727 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 23:04:23 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-11 23:04:19 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:04:04 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.013 |  |
| 2026-07-11 23:03:44 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:03:20 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-07-11 23:03:16 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.637 |  |
| 2026-07-11 23:03:15 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:02:57 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:02:30 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:02:26 | Dunamale (Aththanagalu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:02:18 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:02:14 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-07-11 23:02:14 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-07-11 23:02:07 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:01:40 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:01:15 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-07-11 23:01:05 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-07-11 23:00:55 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:00:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:00:28 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-11 22:42:32 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.637 |  |
| 2026-07-11 22:23:19 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.008 |  |
| 2026-07-11 22:18:29 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.013 |  |
| 2026-07-11 22:16:06 | Dunamale (Aththanagalu Oya) | 1.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 23:01:05 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-07-11 22:10:11 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-11 22:05:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-11 17:01:05 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 23:04:23 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-11 23:03:15 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:02:30 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:00:55 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:02:18 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 22:06:32 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:00:48 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:04:28 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 22:06:22 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-11 22:03:41 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 22:12:37 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:01:40 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 22:07:19 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:00:28 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:02:26 | Dunamale (Aththanagalu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:02:57 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:03:44 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:00:48 | Thanthirimale (Malwathu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:02:07 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:04:19 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 22:01:17 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 23:01:15 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-11 22:23:19 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.008 |  |
| 2026-07-11 22:08:06 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-07-11 22:07:39 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.010 |  |
| 2026-07-11 22:05:07 | Thalgahagoda (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-07-11 22:03:14 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-07-11 23:02:14 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-07-11 23:04:04 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.013 |  |
| 2026-07-11 23:03:20 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-07-11 23:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.021 |  |
| 2026-07-11 22:03:46 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.029 |  |
| 2026-07-11 23:02:14 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-07-11 22:04:49 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.037 |  |
| 2026-07-11 23:03:16 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.637 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)