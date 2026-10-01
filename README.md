# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_02:08:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,459 measurements** from **39** stations.
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
| 2026-10-02 02:08:51 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-02 02:07:26 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-02 02:06:47 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.012 |  |
| 2026-10-02 02:06:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:06:19 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.742 |  |
| 2026-10-02 02:06:16 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:05:30 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-02 02:05:14 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:04:44 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-02 02:04:42 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.742 |  |
| 2026-10-02 02:04:02 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:03:45 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-10-02 02:03:40 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.006 |  |
| 2026-10-02 02:03:35 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.041 |  |
| 2026-10-02 02:03:30 | Rathnapura (Kalu Ganga) | 2.67 | 🟢 Normal | -0.133 |  |
| 2026-10-02 02:03:23 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:03:09 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:03:04 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-02 02:02:53 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.090 |  |
| 2026-10-02 02:02:45 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.040 |  |
| 2026-10-02 02:02:03 | Thawalama (Gin Ganga) | 2.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-02 02:01:50 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:01:38 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-02 02:01:36 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:01:27 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-02 02:01:01 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.024 |  |
| 2026-10-02 02:01:00 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:00:46 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-02 01:42:44 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:39:32 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-02 01:33:06 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-02 01:30:56 | Hanwella (Kelani Ganga) | 1.73 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-02 01:28:12 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.135 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 01:02:50 | Panadugama (Nilwala Ganga) | 3.89 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-10-02 01:28:12 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-01 23:08:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-02 02:01:38 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-02 01:39:32 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-02 02:03:04 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-02 02:05:30 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-02 02:00:46 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-02 02:02:03 | Thawalama (Gin Ganga) | 2.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-02 02:04:44 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-02 02:01:27 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-02 02:07:26 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-02 02:08:51 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-02 02:03:09 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:01:00 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:03:23 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:05:14 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:09:37 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:01:36 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:01:50 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:04:02 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:06:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:06:16 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:00:58 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-02 01:42:44 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-02 02:03:45 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-10-02 02:03:40 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.006 |  |
| 2026-10-01 20:33:59 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.006 |  |
| 2026-10-01 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-02 02:06:47 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.012 |  |
| 2026-10-02 01:09:30 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-10-02 01:01:12 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-10-02 02:01:01 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.024 |  |
| 2026-10-02 02:02:45 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.040 |  |
| 2026-10-02 02:03:35 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.041 |  |
| 2026-10-02 02:02:53 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.090 |  |
| 2026-10-02 02:03:30 | Rathnapura (Kalu Ganga) | 2.67 | 🟢 Normal | -0.133 |  |
| 2026-10-02 01:01:31 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | -0.205 |  |
| 2026-10-02 02:06:19 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.742 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)