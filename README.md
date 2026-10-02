# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_08:28:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,691 measurements** from **39** stations.
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
| 2026-10-02 08:28:58 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 08:26:28 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:16:21 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:09:38 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-10-02 08:09:10 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:08:33 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:07:46 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.119 |  |
| 2026-10-02 08:07:29 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | -0.010 |  |
| 2026-10-02 08:06:41 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-02 08:06:34 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:05:52 | Glencourse (Kelani Ganga) | 10.53 | 🟢 Normal | -0.073 |  |
| 2026-10-02 08:05:23 | Panadugama (Nilwala Ganga) | 4.04 | 🟢 Normal | -0.050 |  |
| 2026-10-02 08:05:02 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-10-02 08:04:20 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:04:20 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:04:08 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.081 |  |
| 2026-10-02 08:03:47 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-02 08:03:43 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-02 08:03:32 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-10-02 08:03:26 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 08:03:24 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-02 08:03:20 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-10-02 08:03:19 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:03:17 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:02:57 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:02:44 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:02:36 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 08:02:36 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:02:24 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.039 |  |
| 2026-10-02 08:02:24 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-02 08:02:05 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:02:03 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.023 |  |
| 2026-10-02 08:01:31 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 08:01:25 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.063 |  |
| 2026-10-02 08:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:00:59 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:00:51 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:00:49 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 08:06:41 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-02 08:03:47 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-02 08:03:43 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-02 08:02:24 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-02 08:28:58 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 08:03:26 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 08:02:36 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 08:01:31 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 08:08:33 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:03:19 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:00:51 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:06:34 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:16:21 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:02:57 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:02:44 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:03:17 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:00:59 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:04:20 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:04:20 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:02:36 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:09:10 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:00:49 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:26:28 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:02:05 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-10-02 08:07:29 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | -0.010 |  |
| 2026-10-02 08:03:32 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-10-02 08:03:24 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-02 08:05:02 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-10-02 08:09:38 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-10-02 08:02:03 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.023 |  |
| 2026-10-02 08:03:20 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-10-02 08:02:24 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.039 |  |
| 2026-10-02 08:05:23 | Panadugama (Nilwala Ganga) | 4.04 | 🟢 Normal | -0.050 |  |
| 2026-10-02 08:01:25 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.063 |  |
| 2026-10-02 08:05:52 | Glencourse (Kelani Ganga) | 10.53 | 🟢 Normal | -0.073 |  |
| 2026-10-02 08:04:08 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.081 |  |
| 2026-10-02 08:07:46 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)