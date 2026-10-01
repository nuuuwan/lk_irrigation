# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_00:31:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,398 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 00:31:58 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:27:55 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:19:06 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.028 |  |
| 2026-10-02 00:09:43 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:08:55 | Peradeniya (Mahaweli Ganga) | 3.46 | 🟢 Normal | -0.058 |  |
| 2026-10-02 00:07:59 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.024 |  |
| 2026-10-02 00:07:34 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.028 |  |
| 2026-10-02 00:07:03 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-02 00:05:26 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-10-02 00:05:05 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 56.842 | 🔺 Rising |
| 2026-10-02 00:05:00 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:04:59 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.077 |  |
| 2026-10-02 00:04:52 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.070 |  |
| 2026-10-02 00:04:46 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 56.842 | 🔺 Rising |
| 2026-10-02 00:04:41 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:04:39 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.039 |  |
| 2026-10-02 00:04:37 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:03:38 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-02 00:03:26 | Ellagawa (Kalu Ganga) | 5.39 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-10-02 00:03:17 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.072 |  |
| 2026-10-02 00:03:12 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-02 00:03:04 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-10-02 00:03:04 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-02 00:02:53 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:02:22 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 00:02:21 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:02:09 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:02:01 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:01:50 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:01:40 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.021 |  |
| 2026-10-02 00:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.069 |  |
| 2026-10-02 00:00:51 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-02 00:00:41 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 00:05:05 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 56.842 | 🔺 Rising |
| 2026-10-02 00:03:04 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-10-02 00:03:26 | Ellagawa (Kalu Ganga) | 5.39 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-10-02 00:03:12 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-01 23:08:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-02 00:03:38 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-02 00:07:03 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-02 00:03:04 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-02 00:00:51 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-02 00:02:22 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 00:31:58 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:02:01 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:02:21 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:27:55 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:09:37 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:02:09 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:02:01 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:09:43 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:05:00 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:04:37 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:02:53 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:04:41 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:00:58 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:03:35 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:01:50 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-01 20:33:59 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.006 |  |
| 2026-10-02 00:05:26 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-10-01 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-02 00:00:41 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-02 00:01:40 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.021 |  |
| 2026-10-02 00:07:59 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.024 |  |
| 2026-10-02 00:07:34 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.028 |  |
| 2026-10-02 00:19:06 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.028 |  |
| 2026-10-02 00:04:39 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.039 |  |
| 2026-10-02 00:08:55 | Peradeniya (Mahaweli Ganga) | 3.46 | 🟢 Normal | -0.058 |  |
| 2026-10-02 00:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.069 |  |
| 2026-10-02 00:04:52 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.070 |  |
| 2026-10-02 00:03:17 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.072 |  |
| 2026-10-02 00:04:59 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)