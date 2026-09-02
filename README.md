# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_21:20:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **250,149 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 21:20:51 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-02 21:12:37 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.085 |  |
| 2026-09-02 21:12:22 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.046 |  |
| 2026-09-02 21:10:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-02 21:09:43 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:09:43 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -18.000 |  |
| 2026-09-02 21:09:41 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -18.000 |  |
| 2026-09-02 21:09:08 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.039 |  |
| 2026-09-02 21:08:22 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-02 21:07:32 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:07:26 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-09-02 21:07:21 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-09-02 21:06:55 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 21:06:29 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:06:18 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:06:04 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.009 |  |
| 2026-09-02 21:05:58 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:05:44 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:05:33 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:05:26 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:05:08 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:05:02 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 21:04:43 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-02 21:04:35 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:03:08 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:03:08 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 21:03:08 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:03:01 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:02:57 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-02 21:02:55 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:02:33 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:02:16 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-09-02 21:02:07 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:01:57 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:01:14 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-09-02 21:01:09 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.081 |  |
| 2026-09-02 21:00:49 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 21:01:14 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-09-02 21:10:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-02 21:08:22 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-02 21:04:43 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-02 21:02:57 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-02 21:05:02 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 21:03:08 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 21:06:55 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 21:20:51 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-02 21:00:49 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:03:08 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:06:29 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:05:58 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:09:43 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:05:08 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 18:04:32 | Galgamuwa (Mee Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:02:07 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:02:55 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:07:32 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:03:01 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:01:57 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:05:26 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:02:33 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:05:44 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:03:08 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-02 18:03:25 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:06:18 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:04:35 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-02 21:07:21 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-09-02 21:06:04 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.009 |  |
| 2026-09-02 21:02:16 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-09-02 21:07:26 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.019 |  |
| 2026-09-02 21:09:08 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.039 |  |
| 2026-09-02 18:00:38 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.040 |  |
| 2026-09-02 21:12:22 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.046 |  |
| 2026-09-02 21:01:09 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.081 |  |
| 2026-09-02 21:12:37 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.085 |  |
| 2026-09-02 21:09:43 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)