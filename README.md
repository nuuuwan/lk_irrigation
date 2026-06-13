# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--14_03:12:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **178,787 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 03:12:24 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:10:18 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:09:56 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:09:09 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.003 |  |
| 2026-06-14 03:07:21 | Rathnapura (Kalu Ganga) | 4.24 | 🟢 Normal | -2.298 |  |
| 2026-06-14 03:06:46 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -4.500 |  |
| 2026-06-14 03:06:30 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -4.500 |  |
| 2026-06-14 03:06:12 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -4.500 |  |
| 2026-06-14 03:05:50 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:05:49 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | -0.031 |  |
| 2026-06-14 03:05:01 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-06-14 03:05:00 | Rathnapura (Kalu Ganga) | 4.33 | 🟢 Normal | -2.298 |  |
| 2026-06-14 03:04:19 | Hanwella (Kelani Ganga) | 3.84 | 🟢 Normal | -0.020 |  |
| 2026-06-14 03:04:11 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:04:11 | Glencourse (Kelani Ganga) | 11.62 | 🟢 Normal | -0.031 |  |
| 2026-06-14 03:03:53 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.097 |  |
| 2026-06-14 03:03:42 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-06-14 03:03:30 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | -0.034 |  |
| 2026-06-14 03:03:18 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 03:03:17 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-06-14 03:03:14 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | -0.031 |  |
| 2026-06-14 03:03:09 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.130 |  |
| 2026-06-14 03:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-06-14 03:03:02 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.020 |  |
| 2026-06-14 03:02:57 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-14 03:02:57 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-06-14 03:02:45 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.032 |  |
| 2026-06-14 03:02:42 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:02:39 | Dunamale (Aththanagalu Oya) | 3.21 | 🟢 Normal | -0.020 |  |
| 2026-06-14 03:02:16 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.062 |  |
| 2026-06-14 03:02:11 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-06-14 03:01:59 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:01:56 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:01:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | 0.000 |  |
| 2026-06-14 03:00:53 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:59:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | 0.000 |  |
| 2026-06-14 02:58:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-14 03:01:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.54 | 🟠 Minor Flood | 0.000 |  |
| 2026-06-14 03:03:17 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-06-13 18:01:49 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-14 03:03:18 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-14 03:12:24 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:00:53 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:01:43 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:01:59 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:09:56 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:02:42 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:10:18 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-14 02:02:30 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:04:11 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:05:50 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:01:56 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-14 03:09:09 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.003 |  |
| 2026-06-14 03:02:57 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-06-14 03:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-06-14 03:02:57 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-06-14 03:02:11 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-06-14 03:03:42 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.019 |  |
| 2026-06-14 01:04:23 | Giriulla (Maha Oya) | 2.14 | 🟢 Normal | -0.020 |  |
| 2026-06-14 03:04:19 | Hanwella (Kelani Ganga) | 3.84 | 🟢 Normal | -0.020 |  |
| 2026-06-14 03:05:01 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-06-14 03:02:39 | Dunamale (Aththanagalu Oya) | 3.21 | 🟢 Normal | -0.020 |  |
| 2026-06-14 03:03:02 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.020 |  |
| 2026-06-13 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.021 |  |
| 2026-06-14 02:02:13 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | -0.021 |  |
| 2026-06-14 03:05:49 | Putupaula (Kalu Ganga) | 2.70 | 🟢 Normal | -0.031 |  |
| 2026-06-14 03:04:11 | Glencourse (Kelani Ganga) | 11.62 | 🟢 Normal | -0.031 |  |
| 2026-06-14 03:03:14 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | -0.031 |  |
| 2026-06-14 03:02:45 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.032 |  |
| 2026-06-14 03:03:30 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | -0.034 |  |
| 2026-06-13 18:05:47 | Galgamuwa (Mee Oya) | 1.44 | 🟢 Normal | -0.040 |  |
| 2026-06-14 03:02:16 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.062 |  |
| 2026-06-14 03:03:53 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.097 |  |
| 2026-06-14 03:03:09 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.130 |  |
| 2026-06-14 03:07:21 | Rathnapura (Kalu Ganga) | 4.24 | 🟢 Normal | -2.298 |  |
| 2026-06-14 03:06:46 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -4.500 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)