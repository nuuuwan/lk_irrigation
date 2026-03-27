# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--27_13:31:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **108,785 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 13:31:38 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:15:23 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | -0.009 |  |
| 2026-03-27 13:14:30 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:11:08 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-03-27 13:08:11 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:08:03 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:06:57 | Rathnapura (Kalu Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-03-27 13:06:49 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | -3.269 |  |
| 2026-03-27 13:06:32 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.039 |  |
| 2026-03-27 13:05:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.028 |  |
| 2026-03-27 13:05:44 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:05:40 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:05:34 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-03-27 13:05:23 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-03-27 13:05:21 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.019 |  |
| 2026-03-27 13:05:11 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 13:04:55 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:04:41 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:04:34 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:04:22 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:04:10 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:03:46 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:03:46 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:03:38 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:03:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-27 13:02:50 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-27 13:02:40 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.049 |  |
| 2026-03-27 13:02:21 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:01:46 | Ellagawa (Kalu Ganga) | 3.71 | 🟢 Normal | 4.188 | 🔺 Rising |
| 2026-03-27 13:01:37 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-27 13:01:34 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:01:30 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:01:25 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:01:24 | Weraganthota (Mahaweli Ganga) | -2.53 | 🟢 Normal | -0.261 |  |
| 2026-03-27 13:01:22 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:01:17 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:01:06 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:00:53 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:00:44 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:00:32 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-27 13:01:46 | Ellagawa (Kalu Ganga) | 3.71 | 🟢 Normal | 4.188 | 🔺 Rising |
| 2026-03-27 13:03:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-27 13:01:37 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-27 13:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-27 13:05:11 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-27 13:01:34 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:00:53 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:01:06 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:02:21 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:01:22 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:14:30 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:31:38 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:01:17 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:04:34 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:03:46 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:04:22 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:05:40 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:03:38 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:04:10 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:04:41 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:02:50 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:05:44 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:04:55 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:00:44 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:08:03 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:01:30 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:08:11 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:01:25 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-27 13:11:08 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-03-27 13:15:23 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | -0.009 |  |
| 2026-03-27 13:05:23 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-03-27 13:05:21 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.019 |  |
| 2026-03-27 13:05:34 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-03-27 13:06:57 | Rathnapura (Kalu Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-03-27 13:05:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.028 |  |
| 2026-03-27 13:06:32 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.039 |  |
| 2026-03-27 13:02:40 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.049 |  |
| 2026-03-27 13:01:24 | Weraganthota (Mahaweli Ganga) | -2.53 | 🟢 Normal | -0.261 |  |
| 2026-03-27 13:06:49 | Putupaula (Kalu Ganga) | 0.18 | 🟢 Normal | -3.269 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)