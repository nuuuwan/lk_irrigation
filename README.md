# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_08:06:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,739 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 08:06:41 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 3.833 | 🔺 Rising |
| 2026-03-16 08:06:29 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-03-16 08:06:02 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:05:46 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-16 08:05:15 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.082 |  |
| 2026-03-16 08:04:36 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-03-16 08:04:03 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:03:59 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:03:55 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:03:54 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:03:47 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:03:39 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-16 08:03:38 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.050 |  |
| 2026-03-16 08:03:22 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-16 08:03:17 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:03:12 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:03:01 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-16 08:02:57 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.017 |  |
| 2026-03-16 08:02:41 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:02:38 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-03-16 08:02:19 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:02:17 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.011 |  |
| 2026-03-16 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.070 |  |
| 2026-03-16 08:02:14 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.114 |  |
| 2026-03-16 08:02:10 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.011 |  |
| 2026-03-16 08:01:42 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:01:41 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-16 08:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-03-16 08:01:27 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:01:22 | Nagalagam Street (Kelani Ganga) | 0.23 | 🟢 Normal | -0.047 |  |
| 2026-03-16 08:01:00 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-16 08:00:49 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:00:47 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:00:47 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.031 |  |
| 2026-03-16 08:00:37 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.033 |  |
| 2026-03-16 07:59:29 | Thawalama (Gin Ganga) | 0.81 | 🟢 Normal | 3.833 | 🔺 Rising |
| 2026-03-16 07:51:52 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:34:08 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:28:41 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.082 |  |
| 2026-03-16 07:27:09 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.017 |  |
| 2026-03-16 07:22:25 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:14:52 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:12:43 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 3.833 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 08:06:41 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 3.833 | 🔺 Rising |
| 2026-03-16 08:05:46 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-16 08:01:00 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-16 08:01:41 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-16 08:03:54 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:01:42 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:03:17 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:06:12 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:03:47 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:00:47 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:03:59 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:01:27 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-16 07:34:08 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:00:49 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:04:03 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:06:02 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:03:12 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:02:41 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:03:55 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:02:19 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-16 08:03:01 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-03-16 08:03:22 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-16 08:03:39 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-16 07:11:45 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-03-16 08:02:10 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | -0.011 |  |
| 2026-03-16 08:02:17 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.011 |  |
| 2026-03-16 08:02:57 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.017 |  |
| 2026-03-16 08:04:36 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2026-03-16 08:06:29 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-03-16 08:01:31 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-03-16 08:02:38 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-03-16 08:00:47 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.031 |  |
| 2026-03-16 08:00:37 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.033 |  |
| 2026-03-16 08:01:22 | Nagalagam Street (Kelani Ganga) | 0.23 | 🟢 Normal | -0.047 |  |
| 2026-03-16 08:03:38 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.050 |  |
| 2026-03-16 08:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.070 |  |
| 2026-03-16 08:05:15 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.082 |  |
| 2026-03-16 08:02:14 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.114 |  |
| 2026-03-16 07:06:33 | Baddegama (Gin Ganga) | 0.34 | 🟢 Normal | -69.231 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)