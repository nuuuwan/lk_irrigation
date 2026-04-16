# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--16_21:11:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,952 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 21:11:51 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.049 |  |
| 2026-04-16 21:11:34 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.035 |  |
| 2026-04-16 21:08:55 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-16 21:06:04 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:05:59 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:05:52 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.029 |  |
| 2026-04-16 21:05:47 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:05:22 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2026-04-16 21:05:20 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-04-16 21:04:56 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 21:04:43 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:04:32 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.041 |  |
| 2026-04-16 21:04:14 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:04:11 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.031 |  |
| 2026-04-16 21:03:58 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.040 |  |
| 2026-04-16 21:03:36 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:03:31 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-16 21:03:15 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-16 21:03:07 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-16 21:03:03 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:02:58 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-04-16 21:02:58 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:02:46 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:02:37 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:02:26 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-16 21:02:13 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-16 21:02:11 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.052 |  |
| 2026-04-16 21:02:09 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.010 |  |
| 2026-04-16 21:01:22 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-04-16 21:01:19 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-16 21:01:18 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:01:09 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-16 21:00:58 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:00:15 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:37:31 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-16 20:37:08 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-16 21:01:09 | Peradeniya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-16 21:01:19 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-16 21:08:55 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-16 21:04:56 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-16 21:00:15 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:00:59 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:01:18 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:00:58 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:19 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:03:36 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:04:43 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:02:58 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:05:47 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:02:26 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:06:04 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:05:59 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:04:14 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:56 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:02:46 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:03:03 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-04-16 20:09:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-16 21:02:17 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-16 21:03:15 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-16 21:03:07 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-16 21:02:13 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-16 21:02:09 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.010 |  |
| 2026-04-16 21:05:20 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-04-16 21:03:31 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-04-16 21:01:22 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-04-16 21:02:58 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-04-16 21:05:22 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.022 |  |
| 2026-04-16 21:05:52 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.029 |  |
| 2026-04-16 21:04:11 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.031 |  |
| 2026-04-16 21:11:34 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.035 |  |
| 2026-04-16 21:03:58 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.040 |  |
| 2026-04-16 21:04:32 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.041 |  |
| 2026-04-16 21:11:51 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.049 |  |
| 2026-04-16 21:02:11 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.052 |  |
| 2026-04-16 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -4.696 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)