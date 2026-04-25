# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_09:13:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,514 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 09:13:47 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.022 |  |
| 2026-04-25 09:09:12 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.037 |  |
| 2026-04-25 09:07:55 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | -0.018 |  |
| 2026-04-25 09:06:30 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.020 |  |
| 2026-04-25 09:06:19 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:06:11 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.019 |  |
| 2026-04-25 09:06:05 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-25 09:05:41 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-04-25 09:05:06 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:04:48 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:04:45 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-25 09:04:45 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:04:43 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-04-25 09:04:19 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-25 09:03:58 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-25 09:03:57 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-25 09:03:53 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:03:34 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:03:26 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-04-25 09:03:23 | Katharagama (Menik Ganga) | 1.76 | 🟢 Normal | -0.012 |  |
| 2026-04-25 09:02:54 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.029 |  |
| 2026-04-25 09:02:48 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -0.070 |  |
| 2026-04-25 09:02:10 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.022 |  |
| 2026-04-25 09:01:46 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-25 09:01:43 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:01:35 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.276 |  |
| 2026-04-25 09:01:33 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-04-25 09:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:01:22 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:01:20 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.033 |  |
| 2026-04-25 09:00:57 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.040 |  |
| 2026-04-25 09:00:27 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-25 09:00:17 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:00:07 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.013 |  |
| 2026-04-25 08:42:32 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 09:03:58 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-25 09:04:45 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-25 08:04:16 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-25 09:03:53 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:04:45 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:01:22 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:02:48 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:04:48 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:04:27 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:06:19 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:01:43 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:05:06 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:00:17 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:03:34 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-25 09:05:41 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-04-25 09:06:05 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-25 09:04:19 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-04-25 08:02:51 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-25 09:03:57 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-25 09:03:26 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-04-25 09:00:27 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-25 09:03:23 | Katharagama (Menik Ganga) | 1.76 | 🟢 Normal | -0.012 |  |
| 2026-04-25 09:00:07 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | -0.013 |  |
| 2026-04-25 09:07:55 | Galgamuwa (Mee Oya) | 0.50 | 🟢 Normal | -0.018 |  |
| 2026-04-25 09:06:11 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.019 |  |
| 2026-04-25 09:06:30 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.020 |  |
| 2026-04-25 09:01:46 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-25 09:01:33 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-04-25 09:04:43 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-04-25 09:13:47 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.022 |  |
| 2026-04-25 09:02:10 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.022 |  |
| 2026-04-25 09:02:54 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.029 |  |
| 2026-04-25 09:01:20 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.033 |  |
| 2026-04-25 09:09:12 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.037 |  |
| 2026-04-25 09:00:57 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.040 |  |
| 2026-04-25 09:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | -0.070 |  |
| 2026-04-25 08:05:03 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.093 |  |
| 2026-04-25 09:01:35 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.276 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)