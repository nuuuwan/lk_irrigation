# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--03_09:30:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **63,139 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 09:30:02 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-02-03 09:22:19 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:17:10 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.012 |  |
| 2026-02-03 09:16:43 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | -0.009 |  |
| 2026-02-03 09:14:00 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.018 |  |
| 2026-02-03 09:11:25 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:09:52 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:06:27 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:06:22 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-02-03 09:06:16 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-03 09:05:16 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.044 |  |
| 2026-02-03 09:03:33 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:03:28 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.039 |  |
| 2026-02-03 09:03:26 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:03:21 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-02-03 09:03:18 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-03 09:03:06 | Weraganthota (Mahaweli Ganga) | -2.28 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-02-03 09:02:52 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.085 |  |
| 2026-02-03 09:02:48 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:02:35 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:02:22 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:02:17 | Nagalagam Street (Kelani Ganga) | 0.17 | 🟢 Normal | -0.046 |  |
| 2026-02-03 09:02:09 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:01:58 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.040 |  |
| 2026-02-03 09:01:50 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:01:34 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-02-03 09:01:29 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-03 09:01:16 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:00:53 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 09:03:06 | Weraganthota (Mahaweli Ganga) | -2.28 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-02-03 09:06:22 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-02-03 05:18:55 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-03 05:03:58 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-03 09:03:18 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-03 09:06:16 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-03 09:01:50 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:00:53 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 05:00:50 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:03:33 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:22:19 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:02:48 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:02:22 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:02:35 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:03:26 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:02:09 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:09:52 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:11:25 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-03 09:06:27 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-03 09:16:43 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | -0.009 |  |
| 2026-02-03 06:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-03 09:01:29 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-03 09:17:10 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.012 |  |
| 2026-02-03 09:14:00 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | -0.018 |  |
| 2026-02-03 09:03:21 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-03 09:01:34 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-02-03 09:30:02 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-02-03 09:03:28 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.039 |  |
| 2026-02-03 09:01:58 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.040 |  |
| 2026-02-03 09:05:16 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.044 |  |
| 2026-02-03 09:02:17 | Nagalagam Street (Kelani Ganga) | 0.17 | 🟢 Normal | -0.046 |  |
| 2026-02-03 06:04:03 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.064 |  |
| 2026-02-03 05:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-03 09:02:52 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.085 |  |
| 2026-02-03 06:01:58 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.197 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)