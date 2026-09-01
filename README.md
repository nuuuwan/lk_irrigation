# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_00:25:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **249,370 measurements** from **39** stations.
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
| 2026-09-02 00:25:57 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:21:59 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:20:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-09-02 00:20:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-09-02 00:20:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-09-02 00:17:06 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-09-02 00:14:36 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:11:17 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:08:15 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:07:37 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:07:34 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:07:18 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-02 00:07:07 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:07:05 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:07:04 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:06:25 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:05:41 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.018 |  |
| 2026-09-02 00:05:37 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:05:12 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:04:58 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:04:40 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:04:39 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-09-02 00:04:37 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -738.000 |  |
| 2026-09-02 00:04:27 | Pitabeddara (Nilwala Ganga) | 2.65 | 🟢 Normal | -738.000 |  |
| 2026-09-02 00:03:31 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-02 00:03:23 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:03:20 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:03:16 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:03:14 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:02:51 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-09-02 00:02:41 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:02:24 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.041 |  |
| 2026-09-02 00:01:35 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:01:34 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:00:52 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:00:17 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-09-02 00:00:08 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-09-01 23:59:38 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 00:20:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-09-02 00:03:31 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-01 23:59:38 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-02 00:07:18 | Glencourse (Kelani Ganga) | 9.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-02 00:00:52 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:04:58 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:03:20 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:08:15 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:03:16 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:25:57 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:03:14 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:05:12 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:06:25 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:07:07 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-01 23:02:42 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:02:41 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:01:35 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:05:37 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:01:34 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:21:59 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:03:23 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:07:34 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:14:36 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-09-01 23:01:26 | Manampitiya (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:00:53 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:04:40 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-01 23:01:12 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-02 00:07:37 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-01 18:04:47 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-02 00:00:08 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-09-02 00:02:51 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-09-02 00:04:39 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-09-02 00:05:41 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.018 |  |
| 2026-09-02 00:17:06 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.019 |  |
| 2026-09-02 00:00:17 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-09-02 00:02:24 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.041 |  |
| 2026-09-01 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.060 |  |
| 2026-09-02 00:04:37 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -738.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)