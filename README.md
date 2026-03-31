# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_17:29:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **112,513 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 17:29:46 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | -0.026 |  |
| 2026-03-31 17:11:15 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-31 17:11:08 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-03-31 17:09:44 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:09:24 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:08:24 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:08:22 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:07:53 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:07:42 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:06:45 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.026 |  |
| 2026-03-31 17:06:42 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.078 |  |
| 2026-03-31 17:05:45 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-31 17:05:34 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:04:26 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-03-31 17:04:15 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:04:08 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:04:05 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.127 |  |
| 2026-03-31 17:03:53 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:03:39 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.023 |  |
| 2026-03-31 17:03:31 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 17:03:22 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:03:13 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:03:11 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-03-31 17:03:01 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:02:55 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 17:02:52 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-31 17:02:50 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:02:21 | Giriulla (Maha Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:02:12 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-03-31 17:02:04 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:01:58 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 17:01:00 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-31 17:00:59 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:00:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.094 |  |
| 2026-03-31 17:00:17 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:00:15 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:00:11 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 17:11:08 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-03-31 17:01:00 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-31 17:02:52 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-31 17:11:15 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-31 17:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 17:02:55 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 17:03:31 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 17:03:13 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:00:15 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:03:22 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:07:42 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:02:04 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:02:21 | Giriulla (Maha Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:01:58 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:08:24 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:05:34 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:04:08 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:02:50 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:00:17 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:07:53 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:09:24 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:03:53 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:00:59 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 15:51:23 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:08:22 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:09:44 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:03:01 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-31 17:02:12 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 16:04:42 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.005 |  |
| 2026-03-31 17:05:45 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-31 17:00:11 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | -0.013 |  |
| 2026-03-31 17:04:26 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2026-03-31 17:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-03-31 17:03:11 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-03-31 17:03:39 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.023 |  |
| 2026-03-31 17:29:46 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | -0.026 |  |
| 2026-03-31 17:06:42 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.078 |  |
| 2026-03-31 17:00:53 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.094 |  |
| 2026-03-31 17:04:05 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)