# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--07_18:17:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **91,863 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 18:17:56 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:15:58 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:13:16 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:12:04 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-07 18:09:46 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:08:45 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:08:41 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:08:08 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:07:21 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:06:46 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:06:15 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:06:13 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-07 18:05:47 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-03-07 18:05:13 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-07 18:05:12 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:04:43 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | -0.065 |  |
| 2026-03-07 18:04:16 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:03:55 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:03:44 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:03:39 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 18:02:56 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-03-07 18:05:13 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-07 18:12:04 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-07 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 18:01:07 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:00:12 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:09 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:06:15 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:16 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:09:46 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:36 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:03:07 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:07:21 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:03:44 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:08:45 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:17:56 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:03:39 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:06:46 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:03:14 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:08:41 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:13:16 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:08:08 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:03:55 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:05:12 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:04:16 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:36 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:19 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:04:43 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:15:58 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:33 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-03-07 18:06:13 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-07 18:03:18 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-03-07 18:01:56 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.010 |  |
| 2026-03-07 18:05:47 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-03-07 18:03:00 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-03-07 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | -0.065 |  |
| 2026-03-07 18:00:12 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.073 |  |
| 2026-03-07 18:00:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)