# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_09:18:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,730 measurements** from **39** stations.
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
| 2026-10-02 09:18:04 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.043 |  |
| 2026-10-02 09:12:36 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:11:21 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.013 |  |
| 2026-10-02 09:11:05 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.061 |  |
| 2026-10-02 09:11:01 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:08:51 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | -0.009 |  |
| 2026-10-02 09:08:22 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-10-02 09:08:20 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:07:54 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-02 09:07:41 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-10-02 09:06:36 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.059 |  |
| 2026-10-02 09:06:31 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:06:22 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-10-02 09:06:10 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.031 |  |
| 2026-10-02 09:05:57 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:04:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:04:36 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-10-02 09:04:24 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.121 |  |
| 2026-10-02 09:04:10 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-02 09:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 09:03:21 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-10-02 09:03:20 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | -0.052 |  |
| 2026-10-02 09:03:09 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.070 |  |
| 2026-10-02 09:03:06 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-02 09:02:55 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:02:53 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2026-10-02 09:02:48 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-10-02 09:02:37 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:02:17 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 09:02:17 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-10-02 09:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:01:59 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 09:01:42 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.030 |  |
| 2026-10-02 09:01:20 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 09:01:15 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:01:05 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:01:05 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:01:02 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 09:00:56 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 09:04:10 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-02 09:00:56 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-02 09:01:02 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 09:01:59 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 09:02:17 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 09:01:20 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 09:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 09:05:57 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:01:05 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:08:20 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:11:01 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:01:05 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:02:55 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:04:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:02:37 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:01:15 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:12:36 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:06:31 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-02 09:08:51 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | -0.009 |  |
| 2026-10-02 09:04:36 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-10-02 09:03:06 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-02 09:07:41 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-10-02 09:07:54 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-02 09:11:21 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.013 |  |
| 2026-10-02 09:02:48 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-10-02 09:03:21 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-10-02 09:08:22 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-10-02 09:06:22 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-10-02 09:01:42 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.030 |  |
| 2026-10-02 09:02:17 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-10-02 09:06:10 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.031 |  |
| 2026-10-02 09:02:53 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2026-10-02 09:18:04 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.043 |  |
| 2026-10-02 09:03:20 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | -0.052 |  |
| 2026-10-02 09:06:36 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.059 |  |
| 2026-10-02 09:11:05 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.061 |  |
| 2026-10-02 09:03:09 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.070 |  |
| 2026-10-02 09:04:24 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)