# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--27_21:23:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **84,797 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 21:23:47 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.025 |  |
| 2026-02-27 21:17:36 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:11:26 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:11:24 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-02-27 21:11:09 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:10:05 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:08:16 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:07:49 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-02-27 21:07:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-02-27 21:07:24 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:06:43 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:06:37 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-02-27 21:05:58 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:05:04 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:05:04 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:04:55 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:04:43 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-27 21:04:42 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.324 |  |
| 2026-02-27 21:04:33 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:04:26 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-27 21:04:05 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-27 21:03:59 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-02-27 21:03:04 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:02:45 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.031 |  |
| 2026-02-27 21:02:35 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-02-27 21:02:35 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:02:35 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:02:29 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-02-27 21:02:28 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:02:20 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:02:12 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.011 |  |
| 2026-02-27 21:02:07 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:01:50 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:01:49 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:01:35 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:01:00 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-27 21:11:24 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-02-27 21:07:32 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-02-27 21:04:43 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-02-27 21:10:05 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-27 20:07:53 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:01:49 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:01:35 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:02:28 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:05:04 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-27 18:13:29 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:05:58 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:05:04 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:02:20 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:01:50 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:06:43 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:08:16 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:02:35 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:02:35 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:04:33 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:11:26 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:17:36 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-27 18:03:42 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:11:09 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:04:55 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:03:04 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-27 21:07:49 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-02-27 21:06:37 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-02-27 21:04:26 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-27 21:02:29 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-02-27 21:03:59 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-02-27 21:04:05 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-27 21:02:35 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-02-27 21:02:12 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.011 |  |
| 2026-02-27 20:09:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.021 |  |
| 2026-02-27 21:23:47 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.025 |  |
| 2026-02-27 18:05:48 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | -0.028 |  |
| 2026-02-27 21:02:45 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.031 |  |
| 2026-02-27 21:04:42 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.324 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)