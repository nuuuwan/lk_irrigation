# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_08:06:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,471 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 08:06:01 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-04-25 08:05:58 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-25 08:05:18 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:05:03 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.093 |  |
| 2026-04-25 08:04:30 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.067 |  |
| 2026-04-25 08:04:27 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:04:26 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-04-25 08:04:16 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-25 08:04:05 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 08:03:54 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:03:51 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:03:43 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.052 |  |
| 2026-04-25 08:03:39 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | -0.039 |  |
| 2026-04-25 08:03:22 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-04-25 08:03:01 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.040 |  |
| 2026-04-25 08:02:51 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-25 08:02:51 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-25 08:02:49 | Galgamuwa (Mee Oya) | 0.52 | 🟢 Normal | -0.026 |  |
| 2026-04-25 08:02:45 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-25 08:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:02:25 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.080 |  |
| 2026-04-25 08:02:19 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-04-25 08:02:08 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-04-25 08:02:07 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-04-25 08:01:53 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-25 08:01:52 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.032 |  |
| 2026-04-25 08:01:37 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:01:37 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:01:20 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:01:04 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.050 |  |
| 2026-04-25 08:00:59 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.010 |  |
| 2026-04-25 08:00:54 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:37:41 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.067 |  |
| 2026-04-25 07:35:53 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.067 |  |
| 2026-04-25 07:32:47 | Ellagawa (Kalu Ganga) | 4.71 | 🟢 Normal | -0.039 |  |
| 2026-04-25 07:20:01 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.093 |  |
| 2026-04-25 07:17:33 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:16:11 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 08:05:58 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-25 08:04:16 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-25 08:04:05 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 08:01:37 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:02:25 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:03:28 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:00:54 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:04:27 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:03:51 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:01:37 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-25 06:04:15 | Katharagama (Menik Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:05:18 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:03:54 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:07:52 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-25 08:01:20 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-04-25 07:05:50 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.009 |  |
| 2026-04-25 08:02:51 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-25 08:02:07 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-04-25 08:00:59 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.010 |  |
| 2026-04-25 07:01:35 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-04-25 08:02:51 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-25 08:02:45 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-04-25 07:09:06 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-04-25 08:01:53 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-25 08:06:01 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-04-25 08:04:26 | Hanwella (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-04-25 08:03:22 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-04-25 08:02:19 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-04-25 08:02:49 | Galgamuwa (Mee Oya) | 0.52 | 🟢 Normal | -0.026 |  |
| 2026-04-25 08:02:08 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-04-25 08:01:52 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.032 |  |
| 2026-04-25 08:03:39 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | -0.039 |  |
| 2026-04-25 08:03:01 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.040 |  |
| 2026-04-25 08:01:04 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.050 |  |
| 2026-04-25 08:03:43 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.052 |  |
| 2026-04-25 08:04:30 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.067 |  |
| 2026-04-25 08:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | -0.080 |  |
| 2026-04-25 08:05:03 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)