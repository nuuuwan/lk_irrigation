# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_15:07:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,962 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 15:07:30 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-02 15:07:14 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-02 15:06:56 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.057 |  |
| 2026-10-02 15:06:55 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-10-02 15:06:49 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | -0.020 |  |
| 2026-10-02 15:06:38 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-02 15:06:31 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:06:08 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | -0.067 |  |
| 2026-10-02 15:05:56 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-02 15:05:54 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:05:39 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 15:05:10 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-02 15:04:47 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-10-02 15:04:43 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:04:38 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:04:34 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | -0.030 |  |
| 2026-10-02 15:04:26 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:03:32 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:03:17 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.030 |  |
| 2026-10-02 15:03:17 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-02 15:03:15 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-02 15:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.99 | 🟢 Normal | -0.020 |  |
| 2026-10-02 15:03:14 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.091 |  |
| 2026-10-02 15:02:54 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.033 |  |
| 2026-10-02 15:02:49 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.012 |  |
| 2026-10-02 15:02:28 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:02:26 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.053 |  |
| 2026-10-02 15:02:23 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:02:21 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:01:38 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:01:30 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:01:29 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:01:13 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-02 15:01:00 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.070 |  |
| 2026-10-02 15:00:38 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-10-02 15:00:13 | Weraganthota (Mahaweli Ganga) | -3.51 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 15:04:47 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-10-02 15:06:55 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-10-02 15:00:28 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-10-02 15:03:15 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-02 15:05:10 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-02 15:05:56 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-02 15:07:30 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-02 15:06:38 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-02 15:03:17 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-02 15:05:39 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-02 15:04:43 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:03:32 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:06:31 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:01:29 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:02:23 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:00:38 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:04:26 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:04:38 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:02:28 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:02:21 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:01:30 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:01:38 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:05:54 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-02 15:00:13 | Weraganthota (Mahaweli Ganga) | -3.51 | 🟢 Normal | -0.010 |  |
| 2026-10-02 15:07:14 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-02 15:01:13 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-02 15:02:49 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.012 |  |
| 2026-10-02 14:06:16 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.014 |  |
| 2026-10-02 15:06:49 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | -0.020 |  |
| 2026-10-02 15:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.99 | 🟢 Normal | -0.020 |  |
| 2026-10-02 15:04:34 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | -0.030 |  |
| 2026-10-02 15:03:17 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.030 |  |
| 2026-10-02 15:02:54 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.033 |  |
| 2026-10-02 15:02:26 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.053 |  |
| 2026-10-02 15:06:56 | Glencourse (Kelani Ganga) | 10.25 | 🟢 Normal | -0.057 |  |
| 2026-10-02 15:06:08 | Ellagawa (Kalu Ganga) | 5.69 | 🟢 Normal | -0.067 |  |
| 2026-10-02 14:17:35 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.067 |  |
| 2026-10-02 15:01:00 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.070 |  |
| 2026-10-02 15:03:14 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)