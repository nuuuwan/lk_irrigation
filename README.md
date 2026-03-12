# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_02:10:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,830 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 02:10:26 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:10:11 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.017 |  |
| 2026-03-13 02:09:28 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-13 02:09:25 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.009 |  |
| 2026-03-13 02:09:07 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 02:08:57 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:08:39 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-03-13 02:08:10 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | -3.262 |  |
| 2026-03-13 02:07:20 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.079 |  |
| 2026-03-13 02:07:03 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | -0.129 |  |
| 2026-03-13 02:06:18 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -108.000 |  |
| 2026-03-13 02:06:17 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -108.000 |  |
| 2026-03-13 02:05:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.043 |  |
| 2026-03-13 02:05:13 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-13 02:04:17 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:04:14 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:03:39 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:03:04 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:03:04 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:02:19 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:02:13 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:01:57 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:01:34 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:01:30 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 02:01:14 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.052 |  |
| 2026-03-13 02:01:10 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-13 02:01:02 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.168 |  |
| 2026-03-13 01:31:46 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:22:37 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.043 |  |
| 2026-03-13 01:21:20 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 22:16:26 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-13 02:08:39 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-03-13 02:01:10 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-13 02:09:28 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-12 22:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 02:01:30 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 02:09:07 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 01:03:57 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 01:03:40 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:31:46 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:01:57 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:10:26 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:00:56 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:05:52 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:04:17 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:04:14 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:03:39 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:08:57 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:02:19 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:03:04 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:04:25 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:03:04 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:03:01 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:01:34 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 01:17:04 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:02:13 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 02:09:25 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.009 |  |
| 2026-03-13 01:02:36 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-13 02:05:13 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-13 02:10:11 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.017 |  |
| 2026-03-13 01:03:11 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.033 |  |
| 2026-03-13 02:05:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.043 |  |
| 2026-03-13 02:01:14 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.052 |  |
| 2026-03-13 02:07:20 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.079 |  |
| 2026-03-12 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.083 |  |
| 2026-03-13 02:07:03 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | -0.129 |  |
| 2026-03-13 02:01:02 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.168 |  |
| 2026-03-13 02:08:10 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | -3.262 |  |
| 2026-03-13 02:06:18 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)