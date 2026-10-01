# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_01:05:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,420 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 01:05:45 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:05:32 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:05:29 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:05:10 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:05:00 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.120 |  |
| 2026-10-02 01:04:58 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.165 |  |
| 2026-10-02 01:04:46 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.029 |  |
| 2026-10-02 01:04:07 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:03:59 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:03:25 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.082 |  |
| 2026-10-02 01:03:24 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:03:04 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | 0.302 | 🔺 Rising |
| 2026-10-02 01:02:50 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-10-02 01:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.138 |  |
| 2026-10-02 01:02:38 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.031 |  |
| 2026-10-02 01:02:18 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:02:17 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.521 | 🔺 Rising |
| 2026-10-02 01:02:04 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-02 01:01:36 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:01:31 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.205 |  |
| 2026-10-02 01:01:12 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-10-02 01:00:45 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:31:58 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:27:55 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 00:05:05 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 56.842 | 🔺 Rising |
| 2026-10-02 01:02:17 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | 0.521 | 🔺 Rising |
| 2026-10-02 01:03:04 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | 0.302 | 🔺 Rising |
| 2026-10-02 01:02:50 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-10-02 00:03:12 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-10-01 23:08:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-02 00:03:38 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-02 00:07:03 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-02 00:00:51 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-02 01:01:36 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:05:45 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:05:10 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:02:18 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:27:55 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:09:37 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:02:09 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:04:07 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:09:43 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:03:59 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:05:29 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:05:32 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:00:58 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-01 23:03:35 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-02 00:01:50 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-01 20:33:59 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.006 |  |
| 2026-10-02 00:05:26 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-10-01 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-02 01:02:04 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | -0.010 |  |
| 2026-10-02 01:01:12 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-10-02 00:07:59 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.024 |  |
| 2026-10-02 00:07:34 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.028 |  |
| 2026-10-02 00:19:06 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.028 |  |
| 2026-10-02 01:04:46 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.029 |  |
| 2026-10-02 01:02:38 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.031 |  |
| 2026-10-02 01:03:25 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.082 |  |
| 2026-10-02 01:05:00 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.120 |  |
| 2026-10-02 01:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.138 |  |
| 2026-10-02 01:04:58 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.165 |  |
| 2026-10-02 01:01:31 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)