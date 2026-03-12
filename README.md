# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_09:12:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,214 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 09:12:16 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.026 |  |
| 2026-03-12 09:11:06 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-12 09:10:33 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:09:31 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-12 09:06:54 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:06:54 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:06:09 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.129 |  |
| 2026-03-12 09:05:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-03-12 09:05:56 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:05:47 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:05:46 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-03-12 09:04:59 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-03-12 09:04:56 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-03-12 09:04:11 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-03-12 09:04:09 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:04:07 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:04:06 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-03-12 09:03:57 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:03:40 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:03:11 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-12 09:03:10 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:03:07 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 09:02:43 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-12 09:02:42 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:02:34 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-12 09:02:19 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:02:18 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:02:16 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:02:14 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-12 09:01:48 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:01:22 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.070 |  |
| 2026-03-12 09:01:12 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-03-12 09:01:11 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.072 |  |
| 2026-03-12 09:01:09 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:01:08 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.052 |  |
| 2026-03-12 09:01:01 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-03-12 09:00:44 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:00:12 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 09:04:59 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-03-12 09:04:06 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-03-12 09:01:12 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-03-12 09:02:34 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-12 09:02:43 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-12 09:03:11 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-12 09:02:14 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-12 09:11:06 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-12 09:09:31 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-12 09:03:07 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-12 09:00:44 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:04:07 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:03:57 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:01:48 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:03:40 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:00:12 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:10:33 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:06:54 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:02:19 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:03:10 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:02:42 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:01:01 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:05:56 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:02:16 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:06:54 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:05:47 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:01:09 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:04:09 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:02:18 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 09:05:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-03-12 09:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-03-12 09:04:11 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | -0.021 |  |
| 2026-03-12 09:04:56 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.021 |  |
| 2026-03-12 09:12:16 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.026 |  |
| 2026-03-12 09:05:46 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-03-12 09:01:08 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.052 |  |
| 2026-03-12 09:01:22 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.070 |  |
| 2026-03-12 09:01:11 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.072 |  |
| 2026-03-12 09:06:09 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)