# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_15:12:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,421 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 15:12:21 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:10:04 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.050 |  |
| 2026-04-28 15:07:48 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.018 |  |
| 2026-04-28 15:07:26 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:07:15 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-04-28 15:06:13 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-28 15:05:54 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | -0.061 |  |
| 2026-04-28 15:05:53 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-28 15:05:41 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-04-28 15:04:42 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-28 15:04:32 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.015 |  |
| 2026-04-28 15:04:19 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:04:17 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 15:04:06 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-28 15:03:56 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 15:03:22 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-28 15:00:49 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-28 15:04:06 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-28 15:04:42 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-28 15:03:23 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 15:02:47 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-28 15:01:22 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-28 15:04:17 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 15:02:10 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:07:26 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:01:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:12:21 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:04:19 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:02:48 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:01:51 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:03:37 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:03:56 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:01:25 | Thanthirimale (Malwathu Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-04-28 14:08:45 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:03:03 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:03:05 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 15:05:41 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-04-28 15:03:16 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-28 15:06:13 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-28 15:01:07 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.010 |  |
| 2026-04-28 15:05:53 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-28 15:02:00 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-04-28 15:04:32 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.015 |  |
| 2026-04-28 15:07:48 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.018 |  |
| 2026-04-28 15:02:42 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-04-28 15:03:31 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.020 |  |
| 2026-04-28 15:07:15 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.020 |  |
| 2026-04-28 15:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.024 |  |
| 2026-04-28 15:02:30 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.030 |  |
| 2026-04-28 15:03:22 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-04-28 15:02:40 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.040 |  |
| 2026-04-28 15:10:04 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.050 |  |
| 2026-04-28 15:05:54 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | -0.061 |  |
| 2026-04-28 15:02:59 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)