# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_04:06:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,517 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 04:06:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:05:22 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-10-02 04:04:09 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.070 |  |
| 2026-10-02 04:03:46 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | -1.072 |  |
| 2026-10-02 04:03:42 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.086 |  |
| 2026-10-02 04:03:34 | Dunamale (Aththanagalu Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-02 04:02:58 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:02:57 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -5.684 |  |
| 2026-10-02 04:02:46 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:02:38 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:02:31 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-10-02 04:02:21 | Glencourse (Kelani Ganga) | 10.77 | 🟢 Normal | -0.021 |  |
| 2026-10-02 04:02:19 | Thawalama (Gin Ganga) | 2.56 | 🟢 Normal | -5.684 |  |
| 2026-10-02 04:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-02 04:01:57 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-02 04:01:55 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-02 04:01:45 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:01:32 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:01:13 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-02 04:01:08 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-02 04:00:50 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 03:57:03 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | -1.072 |  |
| 2026-10-02 03:38:04 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-02 03:35:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-02 03:35:15 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-02 03:26:14 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 03:18:07 | Panadugama (Nilwala Ganga) | 4.12 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-10-02 03:12:36 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-10-02 03:02:08 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-10-02 04:01:13 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-02 03:38:04 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-10-02 04:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-02 04:01:57 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-02 04:01:55 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-02 04:01:08 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-02 03:09:28 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:02:38 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:00:50 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 03:02:30 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:02:46 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:01:45 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:09:37 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-02 03:01:10 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-02 03:04:17 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-02 03:01:52 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:06:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:02:58 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 03:16:06 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:00:58 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-02 03:35:15 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:01:32 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-02 03:06:23 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-01 20:33:59 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.006 |  |
| 2026-10-01 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-02 04:03:34 | Dunamale (Aththanagalu Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-02 04:02:31 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-10-02 04:02:21 | Glencourse (Kelani Ganga) | 10.77 | 🟢 Normal | -0.021 |  |
| 2026-10-02 02:01:01 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.024 |  |
| 2026-10-02 03:17:24 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.024 |  |
| 2026-10-02 04:05:22 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-10-02 03:06:01 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | -0.061 |  |
| 2026-10-02 04:04:09 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.070 |  |
| 2026-10-02 04:03:42 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.086 |  |
| 2026-10-02 04:03:46 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | -1.072 |  |
| 2026-10-02 04:02:57 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -5.684 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)