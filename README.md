# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--25_14:12:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **107,016 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 14:12:51 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:10:35 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:10:18 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-25 14:08:18 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:08:01 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-03-25 14:07:52 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-25 14:07:23 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:06:25 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:06:24 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:06:17 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:05:39 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.012 |  |
| 2026-03-25 14:05:20 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:05:12 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-25 14:05:07 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 14:04:18 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-03-25 14:04:00 | Moragaswewa (Deduru Oya) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:03:58 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-03-25 14:03:41 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:03:39 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:03:29 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:03:26 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.049 |  |
| 2026-03-25 14:03:11 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-25 14:02:52 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.030 |  |
| 2026-03-25 14:02:17 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:02:16 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.068 |  |
| 2026-03-25 14:02:15 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:02:15 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:02:13 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-03-25 14:01:37 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:01:25 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.193 |  |
| 2026-03-25 14:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 14:01:05 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:00:44 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:00:08 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 14:02:13 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-03-25 14:10:18 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-25 14:08:01 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-03-25 14:05:12 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-25 14:05:07 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 14:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 13:13:03 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-25 14:02:17 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:00:08 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:04:00 | Moragaswewa (Deduru Oya) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:03:39 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:02:15 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-25 12:07:00 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:06:25 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:07:23 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-25 13:01:59 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:02:15 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:03:41 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:06:24 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:10:35 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:01:37 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:01:05 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:08:18 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:06:17 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:12:51 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:00:44 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:05:20 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:03:29 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:02:52 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-25 14:07:52 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-25 14:04:18 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-03-25 14:03:11 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-25 14:05:39 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.012 |  |
| 2026-03-25 14:03:58 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-03-25 13:05:05 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-03-25 14:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.030 |  |
| 2026-03-25 14:03:26 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.049 |  |
| 2026-03-25 14:02:16 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.068 |  |
| 2026-03-25 14:01:25 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.193 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)