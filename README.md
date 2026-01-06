# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_10:12:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,089 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 10:12:25 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-01-06 10:12:11 | Manampitiya (Mahaweli Ganga) | 3.35 | 🟡 Alert | 0.209 | 🔺 Rising |
| 2026-01-06 10:09:39 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:09:37 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:06:51 | Padiyathalawa (Maduru Oya) | 2.55 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-01-06 10:06:40 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-01-06 10:06:18 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.033 |  |
| 2026-01-06 10:06:11 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:05:49 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.029 |  |
| 2026-01-06 10:05:40 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:05:01 | Peradeniya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-01-06 10:04:35 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 10:03:58 | Thaldena (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-01-06 10:03:51 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.031 |  |
| 2026-01-06 10:03:49 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:03:30 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-06 10:03:30 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.070 |  |
| 2026-01-06 10:03:17 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.099 |  |
| 2026-01-06 10:03:11 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:03:07 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.061 |  |
| 2026-01-06 10:02:59 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-06 10:02:55 | Nakkala (Kumbukkan Oya) | 2.18 | 🟢 Normal | 0.436 | 🔺 Rising |
| 2026-01-06 10:02:53 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.020 |  |
| 2026-01-06 10:02:36 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:02:35 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:02:22 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:02:10 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 10:01:47 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 10:01:45 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | -0.059 |  |
| 2026-01-06 10:01:39 | Siyambalanduwa (Heda Oya) | 4.61 | 🟡 Alert | 0.365 | 🔺 Rising |
| 2026-01-06 10:01:38 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:01:16 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:01:08 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:00:16 | Weraganthota (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-06 09:29:42 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -0.033 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 10:01:39 | Siyambalanduwa (Heda Oya) | 4.61 | 🟡 Alert | 0.365 | 🔺 Rising |
| 2026-01-06 10:12:11 | Manampitiya (Mahaweli Ganga) | 3.35 | 🟡 Alert | 0.209 | 🔺 Rising |
| 2026-01-06 10:02:55 | Nakkala (Kumbukkan Oya) | 2.18 | 🟢 Normal | 0.436 | 🔺 Rising |
| 2026-01-06 10:06:51 | Padiyathalawa (Maduru Oya) | 2.55 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-01-06 10:05:01 | Peradeniya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-01-06 10:02:59 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-06 10:06:40 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-01-06 10:00:16 | Weraganthota (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-06 09:03:33 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-06 10:02:10 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 10:01:47 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 10:04:35 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 10:03:49 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:01:38 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-06 09:05:42 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:03:11 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:09:39 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:05:40 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:02:36 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:01:08 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:02:22 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:09:37 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:06:11 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:01:16 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:02:35 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:02:53 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-06 10:03:30 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-06 10:12:25 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.019 |  |
| 2026-01-06 10:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | -0.020 |  |
| 2026-01-06 10:03:58 | Thaldena (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-01-06 09:13:15 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.022 |  |
| 2026-01-06 09:14:33 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.025 |  |
| 2026-01-06 10:05:49 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.029 |  |
| 2026-01-06 10:03:51 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.031 |  |
| 2026-01-06 10:06:18 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.033 |  |
| 2026-01-06 10:01:45 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | -0.059 |  |
| 2026-01-06 10:03:07 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.061 |  |
| 2026-01-06 10:03:30 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.070 |  |
| 2026-01-06 10:03:17 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)