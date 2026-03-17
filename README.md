# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--17_13:05:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,813 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 13:05:54 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:05:17 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:05:06 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-17 13:04:29 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.076 |  |
| 2026-03-17 13:04:28 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:04:11 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.029 |  |
| 2026-03-17 13:03:59 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:03:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-17 13:03:41 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 13:03:41 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-17 13:03:11 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-17 13:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:02:48 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-17 13:02:42 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-03-17 13:02:35 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:02:34 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:02:29 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-03-17 13:02:29 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-03-17 13:02:04 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-03-17 13:02:00 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-03-17 13:01:48 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:01:46 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:01:44 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:01:19 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.160 |  |
| 2026-03-17 13:01:04 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:01:04 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:11:12 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 13:03:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-17 12:01:38 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-03-17 13:03:11 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-03-17 12:02:11 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-17 13:05:06 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-17 13:03:41 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 12:02:22 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:05:13 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:02:59 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:02:29 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:01:04 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:02:50 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:02:34 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:03:59 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:01:48 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:01:04 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:04:28 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:01:46 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:05:54 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:05:17 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:02:35 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:11:12 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 13:01:44 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-17 12:04:44 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-03-17 13:03:41 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-17 13:02:29 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-03-17 13:02:48 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-03-17 13:02:04 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-03-17 12:04:24 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-17 13:02:00 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2026-03-17 12:04:50 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | -0.013 |  |
| 2026-03-17 13:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-03-17 12:03:47 | Rathnapura (Kalu Ganga) | 0.37 | 🟢 Normal | -0.022 |  |
| 2026-03-17 13:04:11 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.029 |  |
| 2026-03-17 12:01:55 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.030 |  |
| 2026-03-17 13:02:42 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-03-17 12:04:35 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | -0.047 |  |
| 2026-03-17 13:04:29 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.076 |  |
| 2026-03-17 13:01:19 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)