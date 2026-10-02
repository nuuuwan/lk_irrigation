# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_17:06:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,037 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 17:06:30 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.037 |  |
| 2026-10-02 17:06:23 | Thawalama (Gin Ganga) | 2.56 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-10-02 17:06:23 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:06:13 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | -0.021 |  |
| 2026-10-02 17:05:58 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-10-02 17:05:42 | Panadugama (Nilwala Ganga) | 4.08 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-10-02 17:05:29 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-10-02 17:05:23 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:05:13 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.022 |  |
| 2026-10-02 17:05:01 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.039 |  |
| 2026-10-02 17:04:56 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:04:37 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:03:56 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 17:03:47 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-02 17:03:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:03:44 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-10-02 17:03:37 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:03:34 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.040 |  |
| 2026-10-02 17:03:19 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:03:18 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.063 |  |
| 2026-10-02 17:03:13 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.93 | 🟢 Normal | -0.030 |  |
| 2026-10-02 17:02:58 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-02 17:02:28 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 17:02:22 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:02:22 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:02:14 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:01:46 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:01:46 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:01:42 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:01:31 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.040 |  |
| 2026-10-02 17:01:08 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.031 |  |
| 2026-10-02 17:00:52 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 17:05:42 | Panadugama (Nilwala Ganga) | 4.08 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-10-02 17:06:23 | Thawalama (Gin Ganga) | 2.56 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-10-02 17:03:44 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.199 | 🔺 Rising |
| 2026-10-02 16:06:47 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-10-02 17:05:58 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-10-02 17:02:58 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-02 17:03:47 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-02 16:12:26 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-02 17:03:56 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 17:02:28 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 17:02:22 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:03:19 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:04:37 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:01:42 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:00:52 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:03:13 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 16:10:27 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:03:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:01:08 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:05:23 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:06:23 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:02:22 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:03:37 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:01:46 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:02:14 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:04:56 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:05:29 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | -0.009 |  |
| 2026-10-02 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.010 |  |
| 2026-10-02 16:07:37 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-10-02 17:06:13 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | -0.021 |  |
| 2026-10-02 17:05:13 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.022 |  |
| 2026-10-02 16:08:13 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.022 |  |
| 2026-10-02 17:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.93 | 🟢 Normal | -0.030 |  |
| 2026-10-02 17:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.031 |  |
| 2026-10-02 17:06:30 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.037 |  |
| 2026-10-02 17:05:01 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.039 |  |
| 2026-10-02 17:01:31 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.040 |  |
| 2026-10-02 17:03:34 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.040 |  |
| 2026-10-02 17:03:18 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)