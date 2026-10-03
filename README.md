# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_05:41:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,462 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **4** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 05:41:29 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -6.000 |  |
| 2026-10-03 05:41:05 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -6.000 |  |
| 2026-10-03 05:19:10 | Magura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.203 |  |
| 2026-10-03 05:16:10 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 05:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-10-03 05:04:43 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-03 04:05:26 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-03 05:06:22 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-03 05:08:09 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-03 05:05:28 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 05:04:52 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-03 05:01:12 | Ellagawa (Kalu Ganga) | 6.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 04:38:35 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-10-03 05:16:10 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-03 05:00:55 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 05:01:18 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-03 05:02:59 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-03 05:01:47 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:08:06 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-03 05:01:11 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 05:00:19 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-03 05:03:38 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-03 05:04:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-03 05:11:15 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-03 05:01:39 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:06:13 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 05:07:33 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-02 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.010 |  |
| 2026-10-03 05:03:17 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.012 |  |
| 2026-10-03 05:00:57 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-03 05:06:17 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-03 05:03:09 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-10-03 05:01:35 | Hanwella (Kelani Ganga) | 2.61 | 🟢 Normal | -0.021 |  |
| 2026-10-03 05:03:02 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-10-03 05:07:12 | Rathnapura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.028 |  |
| 2026-10-03 05:02:26 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-10-03 05:10:42 | Panadugama (Nilwala Ganga) | 4.60 | 🟢 Normal | -0.048 |  |
| 2026-10-03 05:05:43 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.059 |  |
| 2026-10-03 05:04:06 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.067 |  |
| 2026-10-03 05:19:10 | Magura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.203 |  |
| 2026-10-03 05:03:04 | Glencourse (Kelani Ganga) | 10.76 | 🟢 Normal | -1.312 |  |
| 2026-10-03 05:05:19 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -1.358 |  |
| 2026-10-03 05:41:29 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -6.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)