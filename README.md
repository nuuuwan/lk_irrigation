# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--25_07:00:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **106,713 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 07:00:43 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:00:33 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:00:31 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 06:43:58 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:21:21 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:20:04 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:19:11 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:08:59 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.036 |  |
| 2026-03-25 06:08:40 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-03-25 06:07:51 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-03-25 06:07:11 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:07:09 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:07:00 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.088 |  |
| 2026-03-25 06:06:41 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 06:00:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-03-25 06:00:16 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-03-25 06:01:52 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-25 06:06:15 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-25 06:06:19 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-25 06:05:10 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-25 06:06:01 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-25 06:02:06 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-25 07:00:31 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 05:06:56 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-25 06:06:41 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:00:33 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:01:10 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:05:36 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:20:04 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:00:49 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:04:36 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:21:21 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:07:11 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:02:21 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:05:52 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:01:09 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:00:43 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:03:28 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:03:39 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:08:40 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-03-25 06:07:51 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-03-25 06:04:46 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-25 06:05:10 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-03-25 06:02:09 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-03-25 06:04:02 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-25 06:04:32 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.019 |  |
| 2026-03-25 06:03:59 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-03-25 06:02:14 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-03-25 06:08:59 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.036 |  |
| 2026-03-25 06:04:25 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.083 |  |
| 2026-03-25 06:07:00 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.088 |  |
| 2026-03-25 06:00:54 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.094 |  |
| 2026-03-25 06:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)