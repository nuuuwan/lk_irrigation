# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_21:07:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **109,985 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 21:07:55 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:07:47 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:06:40 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:06:03 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.019 |  |
| 2026-03-28 21:05:12 | Thawalama (Gin Ganga) | 0.85 | 🟢 Normal | -0.049 |  |
| 2026-03-28 21:05:07 | Rathnapura (Kalu Ganga) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-28 21:05:06 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:04:55 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:04:26 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:04:04 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:03:53 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | -0.013 |  |
| 2026-03-28 21:03:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:03:39 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:03:33 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-28 21:03:33 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-03-28 21:03:12 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:03:03 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-28 21:02:45 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:02:28 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.032 |  |
| 2026-03-28 21:02:17 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-28 21:02:07 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:02:04 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:02:02 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:01:48 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:01:45 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-28 21:01:34 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:01:15 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:01:10 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:01:10 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-03-28 21:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-28 20:25:52 | Pitabeddara (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-28 20:19:41 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-28 20:17:55 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 21:02:17 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-03-28 21:03:33 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-28 21:05:07 | Rathnapura (Kalu Ganga) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-28 20:13:19 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-28 21:01:45 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-28 20:19:41 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-28 21:01:15 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:01:34 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:02:02 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:03:47 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:02:04 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-28 20:05:39 | Horowpothana (Yan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-28 18:03:02 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:07:55 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 20:25:52 | Pitabeddara (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:06:40 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:07:47 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:05:06 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:01:48 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:02:45 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:04:04 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:04:55 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:02:07 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:03:39 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-28 18:04:13 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:04:26 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-28 20:04:05 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:01:10 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:03:12 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 20:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-28 21:03:03 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-03-28 21:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-28 21:03:33 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-03-28 21:03:53 | Ellagawa (Kalu Ganga) | 3.65 | 🟢 Normal | -0.013 |  |
| 2026-03-28 21:06:03 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.019 |  |
| 2026-03-28 21:01:10 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-03-28 21:02:28 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.032 |  |
| 2026-03-28 21:05:12 | Thawalama (Gin Ganga) | 0.85 | 🟢 Normal | -0.049 |  |
| 2026-03-28 18:02:29 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.215 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)