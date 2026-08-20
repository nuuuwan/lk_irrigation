# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_06:36:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,346 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 06:36:45 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.001 |  |
| 2026-08-20 06:17:55 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.008 |  |
| 2026-08-20 06:14:01 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:12:24 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-20 06:11:26 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:09:28 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 1.440 | 🔺 Rising |
| 2026-08-20 06:08:55 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:08:38 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 1.440 | 🔺 Rising |
| 2026-08-20 06:07:50 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.010 |  |
| 2026-08-20 06:07:03 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:06:39 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.077 |  |
| 2026-08-20 06:06:21 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.009 |  |
| 2026-08-20 06:06:15 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-08-20 06:06:02 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:06:00 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-20 06:05:52 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:05:11 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-20 06:05:08 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-20 06:05:06 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:05:04 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:05:02 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:05:02 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:05:01 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-20 06:04:56 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:04:29 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:04:06 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:03:57 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-20 06:03:54 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 06:03:23 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:02:56 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:02:44 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:02:03 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-08-20 06:01:58 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.75 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-20 06:01:44 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-08-20 06:01:42 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-20 06:01:35 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:01:31 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:01:16 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:01:09 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:01:06 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:00:56 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-20 06:00:54 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 06:09:28 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | 1.440 | 🔺 Rising |
| 2026-08-20 06:01:44 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-08-20 06:02:03 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-08-20 06:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.75 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-20 06:06:15 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-08-20 06:12:24 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-20 06:00:56 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-20 06:05:01 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-20 06:05:11 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-20 06:03:57 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-20 06:05:08 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-20 06:06:00 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-20 06:01:42 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-20 06:03:54 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 06:01:31 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:01:06 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:11:26 | Moragaswewa (Deduru Oya) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:01:16 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:05:02 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:08:55 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:05:06 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:04:06 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:02:56 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:01:35 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:00:54 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:03:23 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:01:58 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:06:02 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:07:03 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:02:44 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-19 18:02:30 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:14:01 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:01:09 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:04:29 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-20 06:36:45 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.001 |  |
| 2026-08-20 06:17:55 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | -0.008 |  |
| 2026-08-20 06:06:21 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.009 |  |
| 2026-08-20 06:07:50 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | -0.010 |  |
| 2026-08-20 06:06:39 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)