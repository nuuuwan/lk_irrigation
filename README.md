# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_10:01:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,525 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 10:01:11 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-04 10:00:57 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 10:00:54 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-04 10:00:45 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-04 10:00:25 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-04 10:00:20 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:23:12 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:12:22 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-05-04 09:12:00 | Kithulgala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.248 |  |
| 2026-05-04 09:11:19 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:11:15 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:11:07 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.018 |  |
| 2026-05-04 09:11:00 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.037 |  |
| 2026-05-04 09:10:12 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-05-04 09:09:23 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 09:03:31 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-04 09:03:19 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-04 09:01:08 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 10:00:57 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 10:00:25 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-04 10:00:20 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:03:43 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-04 10:01:11 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-04 10:00:54 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:01:57 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:11:19 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:07:57 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:23:12 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:02:21 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:02:04 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:03:41 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:02:33 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:05:16 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:05:12 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:01:55 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-04 10:00:45 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:09:23 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-04 09:12:22 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-05-04 09:10:12 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.009 |  |
| 2026-05-04 09:04:11 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.009 |  |
| 2026-05-04 09:04:30 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-04 09:01:35 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-05-04 09:01:34 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-05-04 09:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-04 09:02:33 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-05-04 09:00:29 | Nagalagam Street (Kelani Ganga) | 0.14 | 🟢 Normal | -0.016 |  |
| 2026-05-04 09:11:07 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.018 |  |
| 2026-05-04 09:11:00 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.037 |  |
| 2026-05-04 09:02:35 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.044 |  |
| 2026-05-04 09:02:28 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.045 |  |
| 2026-05-04 09:06:01 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.051 |  |
| 2026-05-04 09:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.070 |  |
| 2026-05-04 09:02:40 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.094 |  |
| 2026-05-04 09:12:00 | Kithulgala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.248 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)