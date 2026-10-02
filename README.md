# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_22:08:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,213 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 22:08:02 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-02 22:07:28 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-02 22:07:17 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.060 |  |
| 2026-10-02 22:06:38 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.051 |  |
| 2026-10-02 22:06:31 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.036 |  |
| 2026-10-02 22:05:53 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.022 |  |
| 2026-10-02 22:05:33 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:05:27 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:04:35 | Hanwella (Kelani Ganga) | 2.11 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-10-02 22:03:52 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:03:35 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:03:06 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-02 22:02:58 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:02:57 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-02 22:02:43 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-02 22:02:31 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 22:02:30 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-02 22:02:20 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.160 |  |
| 2026-10-02 22:01:55 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:01:39 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.062 |  |
| 2026-10-02 22:01:28 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:01:27 | Ellagawa (Kalu Ganga) | 6.08 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-02 22:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | -0.020 |  |
| 2026-10-02 22:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.021 |  |
| 2026-10-02 22:01:05 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 21:02:59 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-10-02 22:04:35 | Hanwella (Kelani Ganga) | 2.11 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-10-02 22:07:28 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-10-02 22:02:43 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-02 21:02:04 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-02 22:01:27 | Ellagawa (Kalu Ganga) | 6.08 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-02 21:04:05 | Thawalama (Gin Ganga) | 3.26 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-02 22:08:02 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-02 22:02:30 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-02 22:02:57 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-02 22:02:31 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 21:01:16 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:01:05 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:01:28 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 21:02:58 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:08:06 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:03:35 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:03:52 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-02 21:00:57 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:02:58 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:05:33 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:06:13 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:05:27 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-02 22:01:55 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-02 21:06:14 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-02 21:03:23 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-10-02 21:01:56 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.010 |  |
| 2026-10-02 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.010 |  |
| 2026-10-02 21:00:35 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-10-02 22:03:06 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-02 21:05:31 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-10-02 22:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | -0.020 |  |
| 2026-10-02 22:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.021 |  |
| 2026-10-02 22:05:53 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.022 |  |
| 2026-10-02 22:06:31 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | -0.036 |  |
| 2026-10-02 22:06:38 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | -0.051 |  |
| 2026-10-02 22:07:17 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.060 |  |
| 2026-10-02 22:01:39 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.062 |  |
| 2026-10-02 22:02:20 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)