# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_06:41:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,238 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 06:41:26 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:17:14 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:13:45 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-03-20 06:13:44 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-03-20 06:13:13 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.033 |  |
| 2026-03-20 06:13:12 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:11:37 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-03-20 06:11:16 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:10:49 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.092 |  |
| 2026-03-20 06:10:47 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:10:32 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-20 06:09:43 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-20 06:09:26 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.073 |  |
| 2026-03-20 06:08:46 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:07:16 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:06:11 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.039 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 06:13:45 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-03-20 06:11:37 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-03-20 02:03:02 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-03-20 06:04:24 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-03-20 06:00:44 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-03-20 01:13:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-20 06:05:07 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-03-20 06:01:09 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-03-20 06:00:40 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-20 06:05:32 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-20 06:02:35 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-20 06:03:41 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-20 06:06:11 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-20 06:09:43 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-20 06:10:32 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-20 06:01:51 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-20 06:11:16 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:17:14 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:07:16 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:02:08 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:41:26 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:05:25 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:13:12 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:01:45 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:00:24 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:02:23 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:03:45 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:08:46 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-19 18:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 06:05:21 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-03-20 06:05:28 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-20 06:01:39 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-03-20 06:02:09 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-03-20 06:13:13 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.033 |  |
| 2026-03-20 06:09:26 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.073 |  |
| 2026-03-20 06:10:49 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.092 |  |
| 2026-03-20 06:05:13 | Rathnapura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.128 |  |
| 2026-03-20 06:01:27 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.292 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)