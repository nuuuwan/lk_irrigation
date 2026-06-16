# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--16_07:34:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **180,703 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 07:34:10 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-16 07:18:27 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-16 07:17:40 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-16 07:10:44 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:09:41 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:09:12 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.009 |  |
| 2026-06-16 07:08:16 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.018 |  |
| 2026-06-16 07:08:09 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-06-16 07:08:05 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.022 |  |
| 2026-06-16 07:07:44 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-16 07:06:43 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.018 |  |
| 2026-06-16 07:05:43 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-16 07:18:27 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-16 07:04:54 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-16 07:07:44 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-16 07:34:10 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-16 07:17:40 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-16 07:00:07 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-16 07:01:13 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:00:43 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:04:35 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:10:44 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:05:26 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:00:13 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:05:43 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:02:12 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:09:41 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:01:14 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:00:50 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:00:12 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:04:16 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-16 07:09:12 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.009 |  |
| 2026-06-16 07:04:31 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-06-16 07:08:09 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-06-16 07:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.010 |  |
| 2026-06-16 07:03:34 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-06-16 07:02:29 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-06-16 07:01:10 | Ellagawa (Kalu Ganga) | 5.73 | 🟢 Normal | -0.010 |  |
| 2026-06-16 07:02:29 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-06-16 07:00:09 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.016 |  |
| 2026-06-16 07:08:16 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.018 |  |
| 2026-06-16 07:06:43 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.018 |  |
| 2026-06-16 07:03:18 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-06-16 07:03:43 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-06-16 07:04:30 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.021 |  |
| 2026-06-16 07:04:08 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.021 |  |
| 2026-06-16 07:08:05 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.022 |  |
| 2026-06-16 07:02:17 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-06-16 07:00:08 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.060 |  |
| 2026-06-16 07:01:37 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.103 |  |
| 2026-06-16 07:01:46 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.348 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)