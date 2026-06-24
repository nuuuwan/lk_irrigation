# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_10:21:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,988 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 10:21:47 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:18:49 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-24 10:18:41 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:17:26 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.008 |  |
| 2026-06-24 10:16:49 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-06-24 10:16:35 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | -0.016 |  |
| 2026-06-24 10:15:09 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.009 |  |
| 2026-06-24 10:11:00 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-24 10:10:52 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:09:23 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-24 10:07:53 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:06:23 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:06:06 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:05:34 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.019 |  |
| 2026-06-24 10:05:10 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.030 |  |
| 2026-06-24 10:05:10 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-06-24 10:04:28 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.029 |  |
| 2026-06-24 10:04:23 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-06-24 10:04:12 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | -0.059 |  |
| 2026-06-24 10:03:30 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-06-24 10:03:22 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:03:16 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.012 |  |
| 2026-06-24 10:03:14 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | -0.010 |  |
| 2026-06-24 10:03:05 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 10:03:00 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:02:49 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | -0.085 |  |
| 2026-06-24 10:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:02:33 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-24 10:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.34 | 🟡 Alert | -0.060 |  |
| 2026-06-24 10:02:21 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-06-24 10:02:12 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-24 10:02:10 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-06-24 10:01:54 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:01:24 | Ellagawa (Kalu Ganga) | 6.67 | 🟢 Normal | -0.092 |  |
| 2026-06-24 10:01:00 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:00:53 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:00:51 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-06-24 10:00:38 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-06-24 10:00:37 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 10:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.34 | 🟡 Alert | -0.060 |  |
| 2026-06-24 10:02:12 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-24 10:11:00 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-24 10:18:49 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-24 10:02:33 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-24 10:03:05 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-24 10:21:47 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:01:54 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:10:52 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:06:23 | Galgamuwa (Mee Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:03:00 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:03:22 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:01:00 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:07:53 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:18:41 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:06:06 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:00:53 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 10:17:26 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.008 |  |
| 2026-06-24 10:15:09 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.009 |  |
| 2026-06-24 10:16:49 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-06-24 10:02:21 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-06-24 10:09:23 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-24 10:02:10 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-06-24 10:00:38 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-06-24 10:03:14 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | -0.010 |  |
| 2026-06-24 10:03:16 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.012 |  |
| 2026-06-24 10:16:35 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | -0.016 |  |
| 2026-06-24 10:05:34 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.019 |  |
| 2026-06-24 10:04:23 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-06-24 10:00:37 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.020 |  |
| 2026-06-24 10:03:30 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.020 |  |
| 2026-06-24 10:04:28 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.029 |  |
| 2026-06-24 10:00:51 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-06-24 10:05:10 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.030 |  |
| 2026-06-24 10:05:10 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-06-24 10:04:12 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | -0.059 |  |
| 2026-06-24 10:02:49 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | -0.085 |  |
| 2026-06-24 10:01:24 | Ellagawa (Kalu Ganga) | 6.67 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)