# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_02:31:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,253 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 02:31:27 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | -0.045 |  |
| 2026-09-14 02:30:16 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:15:57 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.017 |  |
| 2026-09-14 02:12:43 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:11:02 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-09-14 02:09:41 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.018 |  |
| 2026-09-14 02:07:23 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:07:20 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:06:52 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:06:39 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:05:58 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:05:55 | Ellagawa (Kalu Ganga) | 5.39 | 🟢 Normal | -0.044 |  |
| 2026-09-14 02:05:49 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:04:51 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-09-14 02:04:32 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -36.000 |  |
| 2026-09-14 02:04:30 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -36.000 |  |
| 2026-09-14 02:03:37 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:03:26 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.025 |  |
| 2026-09-14 02:02:35 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:02:31 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-14 02:02:26 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 02:02:26 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-14 02:02:25 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:02:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:02:04 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:02:02 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-09-14 02:02:00 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:01:40 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.073 |  |
| 2026-09-14 02:00:46 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:00:31 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.039 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 02:02:31 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-14 00:03:51 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-14 01:02:16 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-14 01:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-14 02:02:26 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-14 02:02:26 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 02:05:49 | Kithulgala (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:02:39 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:07:23 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:00:46 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:02:25 | Moragaswewa (Deduru Oya) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:30:16 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:02:04 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:02:00 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:13:03 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:01:11 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-14 01:04:17 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:02:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:12:43 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:05:58 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:07:20 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:06:39 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:02:35 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-13 18:04:05 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:03:37 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-14 00:01:48 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-14 02:11:02 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-09-14 02:15:57 | Hanwella (Kelani Ganga) | 1.26 | 🟢 Normal | -0.017 |  |
| 2026-09-14 02:09:41 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.018 |  |
| 2026-09-14 02:02:02 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-09-14 02:03:26 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.025 |  |
| 2026-09-14 02:00:31 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.039 |  |
| 2026-09-14 02:04:51 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-09-14 02:05:55 | Ellagawa (Kalu Ganga) | 5.39 | 🟢 Normal | -0.044 |  |
| 2026-09-14 02:31:27 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | -0.045 |  |
| 2026-09-14 02:01:40 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.073 |  |
| 2026-09-14 01:02:09 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | -0.085 |  |
| 2026-09-14 02:04:32 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)