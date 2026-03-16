# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_10:17:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,819 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 10:17:41 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.017 |  |
| 2026-03-16 10:13:04 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:11:09 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:10:46 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -0.009 |  |
| 2026-03-16 10:09:32 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:09:12 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.047 |  |
| 2026-03-16 10:08:42 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:08:34 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.053 |  |
| 2026-03-16 10:07:30 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:06:48 | Baddegama (Gin Ganga) | 0.71 | 🟢 Normal | -0.061 |  |
| 2026-03-16 10:05:34 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:05:01 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-03-16 10:04:56 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-16 10:04:31 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:04:31 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:03:50 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-16 10:03:45 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.049 |  |
| 2026-03-16 10:03:37 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-16 10:03:24 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:03:17 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:03:13 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:03:11 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:03:10 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-16 10:02:41 | Weraganthota (Mahaweli Ganga) | -2.00 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2026-03-16 10:02:37 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-03-16 10:02:31 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-16 10:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.050 |  |
| 2026-03-16 10:02:01 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-16 10:01:52 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 10:01:50 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:01:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:01:40 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-16 10:01:25 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.049 |  |
| 2026-03-16 10:01:12 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:01:09 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 10:00:58 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:00:51 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-16 10:00:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.093 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 10:02:41 | Weraganthota (Mahaweli Ganga) | -2.00 | 🟢 Normal | 0.336 | 🔺 Rising |
| 2026-03-16 10:00:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-03-16 10:03:10 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-16 10:02:31 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-16 10:02:01 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-16 10:03:37 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-16 10:04:56 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-16 10:01:09 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 10:01:52 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 10:01:50 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:01:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:03:11 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:11:09 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:13:04 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:07:30 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:04:31 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:08:42 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:03:13 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:00:58 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:05:34 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:04:31 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:03:24 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:00:51 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:01:12 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 09:05:43 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:09:32 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-16 10:10:46 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -0.009 |  |
| 2026-03-16 10:05:01 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-03-16 10:03:50 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-03-16 10:02:37 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-03-16 10:00:27 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-16 10:01:40 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-16 10:17:41 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.017 |  |
| 2026-03-16 10:09:12 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.047 |  |
| 2026-03-16 10:01:25 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.049 |  |
| 2026-03-16 10:03:45 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.049 |  |
| 2026-03-16 10:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.050 |  |
| 2026-03-16 10:08:34 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.053 |  |
| 2026-03-16 10:06:48 | Baddegama (Gin Ganga) | 0.71 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)