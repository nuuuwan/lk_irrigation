# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--03_05:20:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,771 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 05:20:11 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:18:11 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | -0.017 |  |
| 2026-03-03 05:17:16 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:16:46 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.085 |  |
| 2026-03-03 05:13:02 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.005 |  |
| 2026-03-03 05:11:27 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:11:25 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:08:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.149 |  |
| 2026-03-03 05:07:49 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-03 05:07:21 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:05:53 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:05:49 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:05:21 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:05:20 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:04:52 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:04:19 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.061 |  |
| 2026-03-03 05:04:16 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-03-03 05:04:06 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:04:02 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.079 |  |
| 2026-03-03 05:03:52 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-03 05:03:19 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.048 |  |
| 2026-03-03 05:02:18 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:01:54 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:01:52 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:01:49 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-03 05:01:44 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-03 05:01:37 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:01:31 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:01:13 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-03-03 05:01:10 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-03 05:00:45 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:00:36 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 05:00:36 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 05:00:12 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 18:07:20 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-03 04:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-03-03 05:07:49 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-03 05:01:49 | Glencourse (Kelani Ganga) | 8.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-03 05:01:10 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-03 05:00:36 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 05:00:36 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 05:04:52 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:00:12 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:00:45 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:01:54 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:17:16 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:20:11 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:00:46 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:11:27 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:01:37 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:05:49 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:05:21 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:01:31 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:01:52 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:05:20 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:05:53 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:02:18 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:11:25 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:04:06 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:07:21 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-03 05:13:02 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.005 |  |
| 2026-03-02 18:03:36 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-03 05:04:16 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-03-03 05:01:44 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-03 05:03:52 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-03-03 05:18:11 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | -0.017 |  |
| 2026-03-03 05:01:13 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-03-03 05:03:19 | Peradeniya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.048 |  |
| 2026-03-03 05:04:19 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.061 |  |
| 2026-03-03 05:04:02 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | -0.079 |  |
| 2026-03-03 05:16:46 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.085 |  |
| 2026-03-03 05:08:45 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)