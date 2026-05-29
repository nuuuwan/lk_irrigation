# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_03:02:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,321 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 03:02:25 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-30 03:02:21 | Rathnapura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.083 |  |
| 2026-05-30 03:02:19 | Magura (Kalu Ganga) | 3.64 | 🟢 Normal | -0.043 |  |
| 2026-05-30 03:02:07 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-30 03:01:54 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 03:01:48 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 03:01:39 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.044 |  |
| 2026-05-30 03:01:13 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 02:13:32 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 02:01:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-30 02:04:18 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-05-30 02:00:32 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-30 02:01:31 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-30 03:02:25 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-30 03:01:13 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 02:01:17 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-30 03:01:54 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-30 02:04:33 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 02:02:30 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:04:21 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 02:02:41 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-30 02:06:33 | Ellagawa (Kalu Ganga) | 8.33 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:02:08 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 03:02:07 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-30 03:01:48 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 02:05:40 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:05:29 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:01:26 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 02:05:37 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-30 02:02:05 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-30 01:06:03 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-30 02:05:32 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | -0.005 |  |
| 2026-05-30 02:01:11 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.005 |  |
| 2026-05-30 01:53:23 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -0.005 |  |
| 2026-05-30 02:03:39 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-30 02:04:37 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-30 02:02:20 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-05-30 02:09:37 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.018 |  |
| 2026-05-30 02:06:50 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | -0.019 |  |
| 2026-05-30 02:04:33 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.020 |  |
| 2026-05-30 01:01:47 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-05-30 02:02:42 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-05-29 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.034 |  |
| 2026-05-30 02:04:24 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.042 |  |
| 2026-05-30 03:02:19 | Magura (Kalu Ganga) | 3.64 | 🟢 Normal | -0.043 |  |
| 2026-05-30 03:01:39 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.044 |  |
| 2026-05-30 02:04:26 | Panadugama (Nilwala Ganga) | 4.29 | 🟢 Normal | -0.071 |  |
| 2026-05-30 03:02:21 | Rathnapura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)