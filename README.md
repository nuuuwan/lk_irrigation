# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--19_06:32:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,812 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 06:32:26 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.002 |  |
| 2026-11-19 06:13:26 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:10:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-19 06:09:19 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:08:47 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-19 06:07:56 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:06:27 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 06:06:26 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 06:05:38 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.023 |  |
| 2026-11-19 06:05:19 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:05:05 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.040 |  |
| 2026-11-19 06:05:04 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:04:19 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:04:14 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-11-19 06:03:48 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 5.538 | 🔺 Rising |
| 2026-11-19 06:03:34 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.029 |  |
| 2026-11-19 06:03:32 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | -0.208 |  |
| 2026-11-19 06:03:28 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-19 06:03:22 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 5.538 | 🔺 Rising |
| 2026-11-19 06:03:09 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-19 06:02:54 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:02:47 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:02:40 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.036 |  |
| 2026-11-19 06:02:30 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.031 |  |
| 2026-11-19 06:02:29 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.011 |  |
| 2026-11-19 06:02:27 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | -0.010 |  |
| 2026-11-19 06:02:18 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-19 06:02:07 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:01:53 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.001 |  |
| 2026-11-19 06:01:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:01:45 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:01:17 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:01:05 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:01:02 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.005 |  |
| 2026-11-19 06:00:32 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:00:31 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:00:19 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:00:10 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 06:03:48 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 5.538 | 🔺 Rising |
| 2026-11-19 06:02:18 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-19 06:10:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-19 06:06:27 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-19 06:06:26 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 06:01:45 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:00:31 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:07:56 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:13:26 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:00:32 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:00:19 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:02:54 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:02:07 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:02:47 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:09:19 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:05:19 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:01:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:01:05 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:00:10 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:01:17 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:10 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:04:19 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:05:04 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-19 06:01:53 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.001 |  |
| 2026-11-19 06:32:26 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.002 |  |
| 2026-11-19 06:01:02 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.005 |  |
| 2026-11-19 06:08:47 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-19 06:02:27 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | -0.010 |  |
| 2026-11-19 06:03:28 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-19 06:03:09 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-19 06:04:14 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-11-19 06:02:29 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.011 |  |
| 2026-11-19 06:05:38 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.023 |  |
| 2026-11-19 06:03:34 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.029 |  |
| 2026-11-19 06:02:30 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.031 |  |
| 2026-11-19 06:02:40 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.036 |  |
| 2026-11-19 06:05:05 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.040 |  |
| 2026-11-19 06:03:32 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | -0.208 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)