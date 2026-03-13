# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_06:17:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,984 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 06:17:16 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-13 06:16:40 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-03-13 06:10:34 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-03-13 06:09:37 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-13 06:08:06 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-03-13 06:07:46 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.065 |  |
| 2026-03-13 06:07:32 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-13 06:07:22 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-13 06:06:53 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.552 | 🔺 Rising |
| 2026-03-13 06:06:39 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:05:33 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-03-13 06:05:27 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-13 06:05:15 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 06:04:56 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 06:04:37 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 06:04:00 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-03-13 06:03:50 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:03:44 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-03-13 06:03:34 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-03-13 06:03:27 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.078 |  |
| 2026-03-13 06:03:11 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 06:03:10 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:03:07 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-13 06:02:38 | Glencourse (Kelani Ganga) | 9.29 | 🟢 Normal | -0.071 |  |
| 2026-03-13 06:02:07 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:01:55 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:01:52 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.042 |  |
| 2026-03-13 06:01:27 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-03-13 06:01:16 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 06:01:10 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:00:51 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-03-13 06:00:46 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:00:32 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:00:18 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-13 06:00:12 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:00:11 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 05:37:37 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.045 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 06:06:53 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.552 | 🔺 Rising |
| 2026-03-13 06:16:40 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-03-13 06:00:51 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-03-13 06:04:00 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.227 | 🔺 Rising |
| 2026-03-13 06:03:34 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-03-13 06:05:27 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-13 06:07:22 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-13 06:03:07 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-13 06:17:16 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-13 06:07:32 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-13 06:09:37 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-13 06:04:56 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 06:00:18 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-13 06:04:37 | Manampitiya (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 06:03:11 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 06:01:16 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 06:00:11 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 06:05:15 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 06:00:32 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:01:55 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:01:10 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:02:07 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:05:52 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:00:46 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:03:10 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:06:39 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-12 18:03:01 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:03:50 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-13 06:08:06 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-03-13 06:05:33 | Badalgama (Maha Oya) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-03-13 06:10:34 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-03-13 06:01:27 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.020 |  |
| 2026-03-13 06:03:44 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-03-13 06:01:52 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.042 |  |
| 2026-03-13 05:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.061 |  |
| 2026-03-13 06:07:46 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.065 |  |
| 2026-03-13 06:02:38 | Glencourse (Kelani Ganga) | 9.29 | 🟢 Normal | -0.071 |  |
| 2026-03-13 06:03:27 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)