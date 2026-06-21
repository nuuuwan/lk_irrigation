# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_06:38:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,136 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **5** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 06:38:00 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.002 |  |
| 2026-06-21 06:18:06 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:12:56 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:11:47 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:09:16 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.042 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 06:00:32 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-21 06:04:28 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-21 06:09:16 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-21 06:06:06 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-21 06:02:18 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-21 06:00:33 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-21 06:02:07 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-21 06:01:46 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 06:38:00 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.002 |  |
| 2026-06-21 06:04:03 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:01:19 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:01:35 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:02:03 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:00:35 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:02:38 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:03:22 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:06:05 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:02:18 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:03:59 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:11:47 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:02:39 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:02:14 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:00:54 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:04:45 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:18:06 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:12:56 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:01:19 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:02:50 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-21 06:07:57 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-06-21 06:04:53 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-06-20 18:02:49 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-06-21 06:02:45 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-06-21 06:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.011 |  |
| 2026-06-21 06:06:38 | Hanwella (Kelani Ganga) | 1.84 | 🟢 Normal | -0.013 |  |
| 2026-06-21 06:00:42 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.052 |  |
| 2026-06-21 06:06:07 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | -0.061 |  |
| 2026-06-21 06:01:26 | Dunamale (Aththanagalu Oya) | 1.45 | 🟢 Normal | -0.116 |  |
| 2026-06-21 06:04:10 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.202 |  |
| 2026-06-21 06:06:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.671 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)