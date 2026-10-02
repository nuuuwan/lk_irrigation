# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_23:06:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,252 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 23:06:57 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.044 |  |
| 2026-10-02 23:06:52 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 23:06:51 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-02 23:06:14 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-02 23:06:13 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-02 23:05:39 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.029 |  |
| 2026-10-02 23:05:24 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:05:07 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.062 |  |
| 2026-10-02 23:04:49 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:04:41 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:04:34 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:04:24 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.068 |  |
| 2026-10-02 23:04:04 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-02 23:03:55 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-10-02 23:03:48 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:03:33 | Glencourse (Kelani Ganga) | 11.28 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-02 23:03:08 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-02 23:02:58 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:02:52 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-10-02 23:02:25 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.005 |  |
| 2026-10-02 23:02:10 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | 1.253 | 🔺 Rising |
| 2026-10-02 23:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-10-02 23:01:55 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-10-02 23:01:49 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:01:27 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:01:24 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:01:15 | Ellagawa (Kalu Ganga) | 6.28 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-10-02 23:01:05 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:00:08 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:57:58 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:56:54 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | 1.253 | 🔺 Rising |
| 2026-10-02 22:34:51 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-10-02 22:25:36 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.044 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 23:06:14 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-02 23:02:10 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | 1.253 | 🔺 Rising |
| 2026-10-02 23:03:55 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-10-02 23:01:55 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-10-02 23:01:15 | Ellagawa (Kalu Ganga) | 6.28 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-10-02 23:06:51 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-02 23:04:04 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-02 22:08:02 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-02 22:02:30 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-02 23:03:33 | Glencourse (Kelani Ganga) | 11.28 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-02 22:02:57 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-02 23:06:52 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 23:02:25 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.005 |  |
| 2026-10-02 23:00:08 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:01:05 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:01:49 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:04:41 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:08:06 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:02:58 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:03:48 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:04:49 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:02:52 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:02:58 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:05:24 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:06:13 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:04:34 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:01:24 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:10:02 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-02 23:02:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-10-02 23:03:08 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-02 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.010 |  |
| 2026-10-02 23:05:39 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.029 |  |
| 2026-10-02 23:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-10-02 22:06:31 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.036 |  |
| 2026-10-02 23:06:57 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.044 |  |
| 2026-10-02 22:06:38 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.051 |  |
| 2026-10-02 23:05:07 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.062 |  |
| 2026-10-02 23:04:24 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.068 |  |
| 2026-10-02 22:13:49 | Thawalama (Gin Ganga) | 3.12 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)