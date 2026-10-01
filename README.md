# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_05:05:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,561 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 05:05:03 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-02 05:04:37 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-02 05:04:26 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-02 05:04:21 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.069 |  |
| 2026-10-02 05:03:55 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-02 05:03:39 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:03:06 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:02:51 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:02:40 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-10-02 05:02:35 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 05:02:30 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.091 |  |
| 2026-10-02 05:02:26 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.020 |  |
| 2026-10-02 05:02:13 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:02:12 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:02:09 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-02 05:02:02 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-02 05:01:56 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:01:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-02 05:01:53 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-10-02 05:01:51 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:01:33 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-02 05:01:32 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -0.099 |  |
| 2026-10-02 05:01:31 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-02 05:01:08 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:00:48 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-10-02 04:47:47 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | -0.006 |  |
| 2026-10-02 04:45:36 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-10-02 04:31:16 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 05:00:48 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-10-02 05:01:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-02 05:04:26 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-02 05:01:31 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-02 05:02:09 | Hanwella (Kelani Ganga) | 2.16 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-02 04:07:52 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-02 05:02:02 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-02 05:04:37 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-02 05:05:03 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-02 04:19:59 | Panadugama (Nilwala Ganga) | 4.16 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-02 05:01:33 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-02 05:02:35 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 05:01:51 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:01:56 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:02:12 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:02:51 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:09:37 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:02:13 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:03:06 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:06:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:03:39 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 03:16:06 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:00:58 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-02 03:35:15 | Urawa (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-02 05:01:08 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-02 04:47:47 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | -0.006 |  |
| 2026-10-02 04:10:01 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-10-02 05:01:53 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-10-02 05:03:55 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-01 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-02 04:31:16 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.016 |  |
| 2026-10-02 05:02:26 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.020 |  |
| 2026-10-02 02:01:01 | Pitabeddara (Nilwala Ganga) | 1.86 | 🟢 Normal | -0.024 |  |
| 2026-10-02 05:02:40 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.030 |  |
| 2026-10-02 05:04:21 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.069 |  |
| 2026-10-02 04:03:42 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.086 |  |
| 2026-10-02 05:02:30 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.091 |  |
| 2026-10-02 05:01:32 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | -0.099 |  |
| 2026-10-02 04:23:03 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)